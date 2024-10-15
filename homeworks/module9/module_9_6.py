from itertools import combinations


def all_variants(text):
    result = []
    for i in range(1, len(text) + 1):
        result += combinations(text, i)
    for _ in result:
        yield _


for el in all_variants('abc'):
    print(''.join(el))
