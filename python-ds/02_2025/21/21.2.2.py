
import math

data = input('r — радиус, h — высота. через пробел:')
r = int(data.split()[0])
h = int(data.split()[1])

side = math.pi * 2 * r * h
s = math.pi * r ** 2
full = side + 2 * s

print('Площадь боковой поверхности (r — радиус, h — высота):', int(side))
print('Полная площадь (S — площадь круга):', int(full))

