from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        self.Name = name
        self.Power = power
        super().__init__()

    def run(self):
        enemies = 100
        print(f"{self.Name}, на нас напали!")
        for i in range(100):
            enemies -= self.Power
            if enemies < 0:
                enemies = 0
            print(f"{self.Name} сражается {i+1} день/дня/дней..., осталось {enemies} воинов.")
            if enemies == 0:
                print(f"{self.Name} одержал победу спустя {i+1} день/дня/дней!")
                break
            sleep(1)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
