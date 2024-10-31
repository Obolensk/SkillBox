import math

r = float(input('Введите радиус случайной планеты: '))

v = 4 / 3 * math.pi * r ** 3

if v < 1.08321 * 10 ** 12:
    delta = 'больше'
else:
    delta = 'меньше'

print('Объем планеты Земля {} в {} раз'.format(delta, round((1.08321 * 10 ** 12) / v, 3)))