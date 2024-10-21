from time import sleep
from threading import Thread


def write_word(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово №{i+1}\n')


class FileWriter:
    def __init__(self, threads_num, *threads_params):
        if threads_num != len(threads_params):
            raise Exception('Не совпадает количество параметров с количеством потоков')

        self.threads = []
        for thread_num in range(threads_num):
            self.threads.append(Thread(target=write_word, args=threads_params[thread_num]))

    def start_all(self):
        for thread in self.threads:
            thread.start()

    def join_all(self):
        for thread in self.threads:
            thread.join()


file_writes = FileWriter(4,
                         (10, 'example1.txt'),
                         (30, 'example2.txt'),
                         (200, 'example3.txt'),
                         (100, 'example4.txt'))

file_writes.start_all()
file_writes.join_all()
