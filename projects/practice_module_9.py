animal = 'Мишка'
animals = ['зайка', 'мишка', 'бегемотик']


def gen_repeat(n):
    def repeat(animal):
        return (animal[:2] + '-') * n + animal

    return repeat


test_1 = gen_repeat(1)
test_2 = gen_repeat(2)

print(test_1(animal))
print(test_2(animal))

repetitions = [gen_repeat(n) for n in range(1, 4)]

result = [func(animal) for func in repetitions]
print(result)

fin_result = [func(x) for func in repetitions for x in animals]
print(fin_result)
