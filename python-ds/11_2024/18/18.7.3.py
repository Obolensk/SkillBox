import random

first = []
second = []
winners = []

for i in range(20):
    first.append(round(random.uniform(5, 10), 2))
    second.append(round(random.uniform(5, 10), 2))
    if first[i] > second[i]:
        winners.append(first[i])
    else:
        winners.append(second[i])


print('Первая команда:', first)
print('Вторая команда:', second)
print('\nПобедители тура:', winners)