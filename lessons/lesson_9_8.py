#Пример 1 - функция, которая возвращает декоратор

import time
import sys

def func_gen_dec(precision):
    def dec(func):
        def wrapper(*args, **kwargs):
            started_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            elapsed = round(ended_at - started_at, precision)
            print(f'Фунцкия работала {elapsed} секунд(ы)')
            return result
        return wrapper
    return dec

def digits(*args):
    total = 1
    for number in args:
        total = number ** 5000
    return len(str(total))

sys.set_int_max_str_digits(10**5)
time_track_precision_6 = func_gen_dec(precision=2)
digits = time_track_precision_6(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)