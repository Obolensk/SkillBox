
while True:
    num_1 = int(input('Введите первое число: '))
    if num_1 > 0 and num_1 < 255:
        break
    else:
        print('Ошибка, попробуйте ещё раз')

while True:
    num_2 = int(input('Введите второе число: '))
    if num_2 > 0 and num_2 < 255:
        break
    else:
        print('Ошибка, попробуйте ещё раз')

while True:
    num_3 = int(input('Введите третье число: '))
    if num_3 > 0 and num_3 < 255:
        break
    else:
        print('Ошибка, попробуйте ещё раз')

while True:
    num_4 = int(input('Введите четвертое число: '))
    if num_4 > 0 and num_4 < 255:
        break
    else:
        print('Ошибка, попробуйте ещё раз')

ip_address = '{0}.{1}.{2}.{3}'.format(
    num_1,
    num_2,
    num_3,
    num_4
)

print('IP-адрес:', ip_address)