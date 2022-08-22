# TODO здесь писать код

N = int(input('Кол-во чисел: '))
list = []
new_list = []

for i in range(N):
    num = int(input('Число: '))
    list.append(num)

print('Последовательность:', list)

list.append(list[0])
new_list.append(list[0])
rev = list[::-1]
add = 1
for i in range(1, len(list)):
    list.insert(-i, list[i])
    rev = list[::-1]
    # print('list', list)
    # print('rev', rev)
    add += 1
    new_list.insert(-i, list[i])
    if list == rev:
        break
print('Нужно добавить чисел: ', add)
print('Сами числа:', new_list)


# Алгоритм решения:
# 1. Проверить не равно равен ли список обратному уже
# 2. Пока не будет равен прибавлять к нему первое число на последнее место,
# потом второе число на предпоследнее место и т.д.

