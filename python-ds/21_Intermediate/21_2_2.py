
import math


def cyl(r, h):
  side = math.pi * 2 * r * h
  full = side + (2 * (math.pi * r ** 2))
  return round(side, 2), round(full, 2)


r = int(input('Радиус: '))
h = int(input('Высота: '))

print('Площадь боковой поверхности и полная площадь', cyl(r, h))

