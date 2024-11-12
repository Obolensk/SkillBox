
my_list = []
n = int(input('Введите число: '))

for i in range(1, n+1):
    if i % 2 != 0:
        my_list.append(i)

print('Список из нечётных чисел от одного до N:', my_list)