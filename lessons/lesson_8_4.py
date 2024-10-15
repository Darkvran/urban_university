from pprint import pprint

"""
3 cпособа генерации функции на лету: (создаются в процессе выполнения кода, а не при комплиляции)
1)Лямбда фунцкия
2)Функция высшего порядка
3)Вызываемый объект
"""

# 1 лямбда-функция

first_example = lambda x: x + 10
print(first_example(x=42))
print(type(first_example))

# 2 лямбда функция с одним аргументом в map()

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_example = map(lambda x: x ** 2, my_numbers)
print(list(second_example))

# 3 лямбда функция с двумя аргументами в map()

third_list_1 = [1, 3, 5, 7, 11]
third_list_2 = [13, 17, 19, 23, 29]
third_example = map(lambda x, y: x + y, third_list_1, third_list_2)
print(list(third_example))

"""
Лямбда функции используются только один раз, а также имеют ограниченное применение, поскольку они могут привести к проблемам с производительностью. Это связано с тем, что они плохо сериализуются
(процесс перехода структуры данных в битовую последовательность). 
"""


# 4 Функция высшего порядка
def get_multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2
    elif n == 3:
        def multiplier(x):
            return x * 3
    else:
        raise Exception('В качестве аргумента принимаются только числа 2 и 3')
    return multiplier


fourth_list = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29]
by_2 = get_multiplier_v1(2)
by_3 = get_multiplier_v1(3)
result = map(by_2, fourth_list)
print(list(result))
result = map(by_3, fourth_list)
print(list(result))

# 5 Замыкание переменных

"""
Замыкание переменной запоминает значение во внешних областях за счет того, что сперва вызывается функция высшего порядка (n в примере ниже находится во внешней области,
и он сохраняется за счет того, что сперва вызвалась функция get_multiplier_v2(n), которая сгенерировала функцию multiplier, где вместо n подставилось конкретное значение.
"""


def get_multiplier_v2(n):
    def multiplier(x):
        return n * x

    return multiplier


by_5 = get_multiplier_v2(5)
print(by_5(x=42))


# 6 Не стоит передавать в аргументы функции изменяемые объекты
def matrix(some_list):
    def multiply_column(x):
        res = []
        for element in some_list:
            res.append(element * x)
        return res

    return multiply_column


sixth_my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sixth_they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
matrix_on_my_numbers = matrix(sixth_my_numbers)
fifth_result = map(matrix_on_my_numbers, sixth_they_numbers)
pprint(list(fifth_result))

sixth_my_numbers.extend([10, 20, 30])
result = map(matrix_on_my_numbers, sixth_they_numbers)
pprint(list(result))
"""
Если передавать изменяемый объект в качестве аргумента, в данном случае могут
возникать непредвиденные ситуации, вроде расширения матрицы при добавлении
в список новых элементов. Поэтому, если нам этого не надо, лучше передавать
в качестве аргумента кортежи
"""

#7 Вызываемая функция

class Multiplier:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return x * self.n

seventh_my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
by_100500 = Multiplier(n=100500)
seventh_result = by_100500(x=42)
print(seventh_result)

seventh_result = map(by_100500, my_numbers)
print(list(seventh_result))