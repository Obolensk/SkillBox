
num_rows = 10
num_cols = 15

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