from threading import Thread
from random import randint
from time import sleep
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        self.Name = name
        super().__init__()

    def run(self):
        sleep(randint(3, 11))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.ochered = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            tableEmpty = 0
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    table.guest.start()
                    print(f"{guest.Name} сел(-а) за стол номер {table.number}")
                    break
                if tableEmpty == len(self.tables)-1:
                    self.ochered.put(guest)
                    print(f"{guest.Name} в очереди")
                tableEmpty += 1

    def discuss_guests(self):
        flag = True
        while flag:
            for table in self.tables:
                if table.guest is not None or self.ochered.empty():
                    if table.guest.is_alive():
                        print(f"{table.guest.Name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None
                    if not self.ochered.empty() and table.guest is None:
                        table.guest = self.ochered.get()
                        print(f"{table.guest.Name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        table.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

for table in cafe.tables:
    table.guest.join()