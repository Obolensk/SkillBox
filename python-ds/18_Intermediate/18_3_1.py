
a = int(input('Введите А: '))
b = int(input('Введите B: '))

list_condition = [i for i in range(a, b + 1) if i % 2 == 0]

print('Список из чётных чисел в диапазоне от А до B', list_condition)