n = int(input('Введите число N: '))
for row in range(n):
    print()
    for col in range(row + 1):
        print(row + 1, end='\t')