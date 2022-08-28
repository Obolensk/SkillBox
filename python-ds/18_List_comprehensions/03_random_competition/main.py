# TODO здесь писать код

import random

first_team = [random.randint(500, 1000)/100 for _ in range(20)]
second_team = [random.randint(500, 1000)/100 for _ in range(20)]
print('Первая команда:', first_team)
print('Вторая команда:', second_team)

winners = [(first_team[i] if first_team[i] > second_team[i] else second_team[i]) for i in range(20)]
print('Победители тура:', winners)