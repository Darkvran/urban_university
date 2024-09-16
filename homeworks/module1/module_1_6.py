my_dict = {"Аска": 2001, "Аянами": 2001, 'Кенджи': 2001, "Наруто": 2002}
print(my_dict)
print(my_dict.get('Аска'))
print(my_dict.get('Саске'))
my_dict.update({'Эрен':2013, 'Люк Скайуокер': 19.5})
print(my_dict.pop('Эрен'))
print(my_dict)

my_set = {'Евангелион', True, 42, 42.0, False, None, True, False, 'Евангелион', 42, 42, 42, 42, 42, 42, 42, 41.999999999999999}
print(my_set)

my_set.update({"Никола Тесла", 666, 666, "Евангелион"})
print(my_set)
my_set.discard(1)
print(my_set)