import math

a = float(input('Введите а: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

disc = b ** 2 - 4 * a * c
if disc < 0:
    print('Корней нет!')
elif disc == 0:
    print('Один корень = ', -b / (a * 2))
else:
    print('Есть два корня этого уравнения!')
    print('Первый корень равен: ', (- b + math.sqrt(disc)) / (a * 2))
    print('Второй корень равен: ', (- b - math.sqrt(disc)) / (a * 2))