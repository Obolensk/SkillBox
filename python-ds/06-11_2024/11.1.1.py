
num = int(input('Введите размер таблицы: '))

for row in range(1, num+1):
    for col in range(1, num+1):
        print(col*row, end='\t')
    print()