# TODO здесь писать код

num = int(input('Количество клеток: '))
not_proper = []
for i in range(num):
    print('Эффективность', i+1, end=' ')
    value = int(input('клетки: '))
    if value < i:
        not_proper.append(value)

print('Неподходящие значения: ', not_proper)
