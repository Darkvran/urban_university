immutable_var = (1, 'string', 3.141, True, None, [1, 2, 3, 4, 5, 6, 7, 8])
print(immutable_var)

#Запись, ведущая к ошибке: (Кортеж - константный объект. Попытка изменить его ведет к ошибке)
#immutable_var[0] = 2

#Допустимая запись. Тут не происходит попытки изменить кортеж, изменяется лишь отдельный объект внутри него..
immutable_var[5][0] = 0
print(immutable_var)

mutable_list = ['1', 2, True, 'Cat', None, 3.1415926]
mutable_list[-1] = True
print(mutable_list)