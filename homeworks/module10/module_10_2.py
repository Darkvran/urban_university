from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        fight_timing = 0
        dirty_xenos_and_heretics = 100
        while dirty_xenos_and_heretics > 0:
            dirty_xenos_and_heretics -= self.power
            sleep(1)
            fight_timing += 1
            print(
                f'{self.name} сражается {fight_timing} день(дня)... Осталось {dirty_xenos_and_heretics} грязных еретиков и ксеносов.')
        print(f'{self.name} одержал победу спустя {fight_timing} дней(дня)! Ура! Слава Императору!')



first_knight = Knight('Sir Lancelot', 10)
first_knight.start()
second_knight = Knight("Sir Galahad", 20)
second_knight.start()
first_knight.join()
second_knight.join()