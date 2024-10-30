# Задача 2. World of tanks

import math

dist = float(input('Введите расстояние до танка: '))
cor = float(input('Введите уголо поворота: '))
cor /= 57.2958

x = dist * math.cos(cor)
y = dist * math.sin(cor)

print('Координаты танка равны ({}, {})'.format(x, y))