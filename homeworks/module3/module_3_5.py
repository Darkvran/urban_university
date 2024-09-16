def get_multiplied_digits(number):
    str_number = str(number)

    if len(str_number) == 1:
        return number

    first = int(str_number[0])

    return first * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(40203))