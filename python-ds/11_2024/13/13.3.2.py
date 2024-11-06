import math

def sphereArea(r):
    s = 4 * math.pi * r ** 2
    print()
    print('Площадь сферы равна', round(s, 2))


def sphereVolume(r):
    v = 4 / 3 * math.pi * r ** 3
    print()
    print('Объем шара равен', round(v, 2))

radius = float(input('Введите радиус: '))
sphereArea(radius)
sphereVolume(radius)