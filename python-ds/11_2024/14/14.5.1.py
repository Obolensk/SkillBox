
num = float(input('Введите число: '))
degree = 0

if num > 1:
    while num > 10:
        num /= 10
        degree += 1
elif num < 1:
    while num < 1:
        num *= 10
        degree -= 1
    num = round(num, 2)



print('Формат плавающей точки: x = {} * 10 ** {}'.format(num, degree))