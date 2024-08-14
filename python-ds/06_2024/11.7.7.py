# levels = int(input('Введите количество уровней пирамиды: '))
levels = 4
level = 0
count = 1

for row in range(levels+2):
    print()
    for col in range(levels + 2):
        if 3 <= (col + row) <= col * 2 - 1:
            print('#' * row, end='')
        else:
            print(' ', end='')


#
# for row in range(levels):
#     for col in range(levels+2):
#         print(' ' * (levels - col), end='')
#         print('#' * (col+1) + '#' * (row+1), end='')
#         print()
