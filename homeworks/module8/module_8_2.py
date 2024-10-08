def personal_sum(numbers):
    sum = 0
    incorrect_data = 0
    try:
        for data in numbers:
            try:
                sum += data
            except:
                incorrect_data += 1
        return (sum, incorrect_data)
    except TypeError:
        return None


def calculate_average(numbers):
    sum = personal_sum(numbers)
    try:
        return sum[0] / (len(numbers) - sum[1])

    except ZeroDivisionError:
        return 0

    except TypeError:
        return 'В numbers записан некорректный тип данных'

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
