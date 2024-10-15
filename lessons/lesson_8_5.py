# Пример 1 - библиотека itertools
import sys
from itertools import repeat

ex_iterator = repeat('4', 100_000)
print(ex_iterator)
print(f'Размер итератора - {sys.getsizeof(ex_iterator)}')


ex_str = "4" * 100_100
print(f'Размер списка - {sys.getsizeof(ex_str)}')