
num = int(input('Введите размер таблицы: '))

for row in range(1, num+1):
    for col in range(1, num+1):
        if row % 2 == 0:
            print(row, end='\t')
        else:
            print(col, end='\t')
    print()