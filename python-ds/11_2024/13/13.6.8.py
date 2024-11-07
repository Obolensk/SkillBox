

a = int(input('Введите первое число: '))
b = int(input('Введите втророе число: '))

# print(max(a, b))
# print(min(a, b))
#
for i in range(max(a, b), 0, -1):
    if max(a, b) % i == 0 and min(a, b) % i == 0:
        print('НОД равен', i)
        break