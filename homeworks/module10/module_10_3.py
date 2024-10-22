from threading import Thread, Lock
from time import sleep
from random import randint
class Bank:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            repl = randint(50, 500)
            self.balance += repl
            print(f'Пополнение: {repl}. Баланс:{self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            taking = randint(50, 500)
            print(f'Запрос на {taking}')
            if taking <= self.balance:
                self.balance -= taking
                print(f'Снятие: {taking}. Баланс:{self.balance}')
            elif taking > self.balance:
                self.lock.acquire()
                print("Запрос отклонён, недостаточно средств")

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
print(f'Итоговый баланс: {bk.balance}')
