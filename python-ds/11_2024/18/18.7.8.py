import random

result = []
n = 10
k = 3
for _ in range(n):
    result.append('|')

print('Количество палок:', n)
print('Количество бросков:', k)

for i in range(k):
    first_stick = random.randint(1, n)
    last_stick = random.randint(first_stick, n)
    print('Бросок {}. Сбиты палки с номера {} по номер {}.'.format(i + 1, first_stick, last_stick))
    lost = ['.' for _ in range(last_stick - first_stick)]
    result = result[0:first_stick] + lost  + result[last_stick:-1]

print('\nРезультат: ', end='')
for i in result:
    print(i, end='')

