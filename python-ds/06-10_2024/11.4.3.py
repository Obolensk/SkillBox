n = int(input('Введите число: '))
for row in range(n+1):
    # print(row)
    for col in range(row, n+1):
        print(col, end=' ')
    print()



