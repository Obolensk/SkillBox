# first_num = int(input('Введите первое число: '))
# second_num = int(input('Введите второе число: '))


a = int(input('Введите четырехзначное число: '))


first = (a % 10000) // 1000
print(first)

second = (a % 1000) // 100
print(second)

third = (a % 100) // 10
print(third)

last = a % 10
print(last)

print('Само число не изменилось', a)