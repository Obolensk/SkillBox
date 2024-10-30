import math

print('Введите стороны треугольника!')
a = float(input('Введите сторону а: '))
b = float(input('Введите сторону b: '))
c = float(input('Введите сторону c: '))

p = (a+b+c)/2
S = math.sqrt(p * (p - a)*(p - b)*(p - c))

print('Площадь треугольника равна:', S)
