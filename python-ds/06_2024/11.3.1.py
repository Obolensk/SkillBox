
num_rows = 20
num_cols = 30

for row in range(num_rows):
    if row == 0:
        print('-' * num_cols)
    else:
        for col in range(num_cols):
            if col == 0 or col == num_cols-1:
                print('|', end='')
            else:
                print(' ', end='')
        print()