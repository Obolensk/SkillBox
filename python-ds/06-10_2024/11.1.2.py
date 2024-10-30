
num = int(input('Введите размер таблицы: '))

for row in range(num+1):
    for col in range(num+1):
        print(col+row, end='\t')
    print()