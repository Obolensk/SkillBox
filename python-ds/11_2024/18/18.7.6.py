import random
before = []
after = []
n = int(input('Количество чисел в списке: '))

for _ in range(n):
    before.append(random.randint(0, 2))

after = [i for i in before if i != 0]

print('Список до сжатия:', before)
print('Список после сжатия:', after)
