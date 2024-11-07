#
# Пример:
#
# Введите первое число: 102
# Введите второе число: 123
#
# Первое число наоборот: 201
# Второе число наоборот: 321
# Сумма: 522
#
# Сумма наоборот: 225


def reverse(a):
    b = 0
    for i in range(1, len(str(a))+1):
        b = b * 10 + int(str(a)[-i])
    return (b)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

a_r = reverse(a)
b_r = reverse(b)

print('Первое число наоборот:', a_r)
print('Второе число наоборот:', b_r)
print('Сумма', a_r + b_r)
print('Сумма наоборот:', reverse(a_r + b_r))