def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)


print_params(5, 2, 'string')
print_params(False, True)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = [5, False, 'string']
values_dict = {'a': "string", 'b': False, 'c': 3.141}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['string', 10]
print_params(*values_list_2, 42)