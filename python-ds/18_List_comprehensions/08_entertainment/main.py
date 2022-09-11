# TODO здесь писать код

N = int(input('Количество палок: ',))
sticks = ['I' for i in range(N)]

print(''.join(sticks))

throws = int(input('Количество бросков: ', ))

for i in range(throws):
    print('Бросок', i+1, '.', end=' ')
    downed_1 = int(input('Сбиты палки с номера ', ))
    downed_2 = int(input('по номер ', ))
    sticks[downed_1-1:downed_2] = ['.'] * (downed_2 - downed_1 + 1)

print(''.join(sticks))
