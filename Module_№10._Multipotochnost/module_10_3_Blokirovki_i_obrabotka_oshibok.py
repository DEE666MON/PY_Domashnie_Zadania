import threading
from time import sleep
from random import randint


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            temp = randint(50, 500)
            self.balance += temp
            print(f"Пополнение: {temp}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            temp = randint(50, 500)
            print(f"Запрос на {temp}")
            if temp <= self.balance:
                self.balance -= temp
                print(f"Снятие: {temp}. Баланс: {self.balance}")
            if temp > self.balance:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
