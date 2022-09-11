# TODO здесь писать код

import random

n = int(input('Количество чисел в списке: '))
list = [random.randint(0, 2) for i in range(n)]

print('Список до сжатия:', list)

new_list = [i for i in list if i != 0]

print('Список после сжатия:', new_list)