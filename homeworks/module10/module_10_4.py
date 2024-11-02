import queue
from threading import Thread
from queue import Queue
from time import sleep
from random import randint


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Table:
    def __init__(self, number, guest: Guest = None):
        self.number = number
        self.guest = guest


class Cafe:
    def __init__(self, *tables: Table):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *quests):
        for quest in quests:
            free_tables = [table for table in self.tables if table.guest is None]
            if len(free_tables) == 0:
                self.queue.put(quest)
                print(f"{quest.name} в очереди.")
            else:
                offered_table = randint(0, len(free_tables)-1)
                free_tables[offered_table].guest = quest
                quest.run()
                print(f'{quest.name} сел(-а) за стол номер {free_tables[offered_table].number}')

    def check_busy_tables(self):
        busy_tables = [table for table in self.tables if table.guest is not None]
        return busy_tables

    def discuss_guests(self):

        while not self.queue.empty() or self.check_busy_tables() is not None:
            busy_tables = self.check_busy_tables()
            for table in busy_tables:
                if not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(F"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        table.guest.run()


tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
