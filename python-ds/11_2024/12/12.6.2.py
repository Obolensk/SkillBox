import math

n = int(input('Введите количество чисел: '))

for i in range(n):
    x = float(input('Введите число: '))
    if x > 0:
        x = math.ceil(x)
        print('x =', x, 'log(x) =', math.log(x))
    else:
        x = math.floor(x)
        print('x =', x, 'exp(x) =', math.exp(x))


