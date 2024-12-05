
n = int(input('Введите длину списка: '))

my_list = []

for i in range(n):
    if i % 2 == 0:
        my_list.append(1)
    else:
        my_list.append(i % 5)

print('Результат:', my_list)