

a = int(input('Введите первое число:'))
b = int(input('Введите втророе число:'))

if a > b:
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            print('')