first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))

summ = first + second
delta = abs(first - second)
double_min = summ - delta
minn = double_min / 2
maximum = summ - minn

print('Максимальное число из пары равняется', abs(maximum))