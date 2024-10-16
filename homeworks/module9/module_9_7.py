def is_prime(func):
    def wrapper(n1, n2, n3):
        func_res = func(n1, n2, n3)
        dividers = []
        for i in range(1, func_res+1):
            if func_res % i == 0:
                dividers.append(i)
        if len(dividers) == 2:
            print('Простое')
            return func_res
        else:
            print('Составное')
            return func_res

    return wrapper


@is_prime
def sum_three(n1, n2, n3):
    return n1 + n2 + n3


result = sum_three(2, 3, 6)
print(result)