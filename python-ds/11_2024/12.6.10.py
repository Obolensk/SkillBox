first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))

maximum = (((first + second) * 2) - (first * 2)) - (((first + second) * 2) - (second * 2))

print(abs(maximum))