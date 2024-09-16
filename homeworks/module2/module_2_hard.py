#right_answers = ['12', '13', '1423','121524', '162534', '13172635', '1218273645', '141923283746', '11029384756', '12131511124210394857', '112211310495867', '1611325212343114105968', '1214114232133124115106978', '1317115262143531341251161079', '11621531441351261171089', '12151811724272163631545414513612711810', '118217316415514613712811910', '13141911923282183731746416515614713812911']


def task(key_number):
    pairs = []
    password = ''
    for i in range(1, key_number):
        for k in range(1, key_number):
            if key_number % (i + k) == 0 and ([str(k), str(i)] not in pairs) and i != k:
                pairs.append([str(i), str(k)])

    for i in range(0, len(pairs)):
        password = password + ''.join(pairs[i])
    return password


print(task(20))

'''
for i in range(3, 21):
    print(i)
    print(task(i) == right_answers[i-3])
'''

#Убрать комментарии для сравнения с ответами