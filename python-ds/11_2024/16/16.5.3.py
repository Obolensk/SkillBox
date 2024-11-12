
cell_num = int(input('Количество клеток: '))
data = []
wrong = []

for i in range(1, cell_num+1):
    print('Эффективность', i, 'клетки: ', end='')
    effect = int(input(''))
    data.append(effect)

print()
print(data)
print()

for i in range(len(data)):
    if data[i] < i:
        wrong.append(data[i])

# print('Неподходящие значения:', wrong)
print('Неподходящие значения:', end=' ')
for i in wrong:
    print(i, end=' ')

