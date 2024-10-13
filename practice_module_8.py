def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    if operation == '+':
        print(f'Результат: {int(operand_1) + int(operand_2)}')
    if operation == '-':
        print(f'Результат: {int(operand_1) - int(operand_2)}')
    if operation == '//':
        print(f'Результат: {int(operand_1) // int(operand_2)}')
    if operation == '/':
        print(f'Результат: {int(operand_1) / int(operand_2)}')
    if operation == '*':
        print(f'Результат: {int(operand_1) * int(operand_2)}')
    if operation == '%':
        print(f'Результат: {int(operand_1) % int(operand_2)}')

cnt = 0

with open('data.txt', 'r') as file:
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Ошибка в линии {cnt}. Не хватает данных для ответа')
            else:
                print(f'Ошибка в линии {cnt}. Нельзя перевести в число')
