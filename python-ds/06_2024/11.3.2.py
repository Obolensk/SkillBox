

for row in range(20):
    if row == 9:
        for i in range(50):
            print('-', end='')
    else:
        for col in range(50):
            if col == 20-row:
                print('/', end='')
            elif col == 28+row:
                print('\\', end='')
            elif col == 24:
                print('|', end='')
            else:
                print(' ', end='')
    print()