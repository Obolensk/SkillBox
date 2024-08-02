
num = int(input('Введите размер матрицы: '))

for row in range(num):
    for col in range(num):
            if col + row < num-1:
                print(0, end='\t')
            elif col + row > num-1:
                print(2, end='\t')
            else:
                print(1, end='\t')
    print()