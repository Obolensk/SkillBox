h = int(input('Введите высоту пирамидки: '))
num = 1
for col in range(h):
    for row in range(h + col):
        if col + row >= h - 1:
            if row % 2 == 0:
                if col % 2 == 0:
                    print(num, end='\t')
                    num += 2
                else:
                    print(' ', end='\t')
            else:
                if col % 2 != 0:
                    print(num, end='\t')
                    num += 2
                else:
                    print(' ', end='\t')
        else:
            print(' ', end='\t')
    print()

