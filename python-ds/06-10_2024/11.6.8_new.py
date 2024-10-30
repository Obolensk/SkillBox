# h = int(input('Введите число: '))
h = 10

for row in range(h):
    for col in range(h*2):
        if row * 2 + 1 > col + row:
            print(h - col, end='')
        elif col + row > h * 2 - 2:
            print(col - h + 1, end='')
        else:
            print('.', end='')
    print()

#
# for row in range(h):
#     for col in range(h*2):
#         if row * 2 < col + row < h * 2 - 1 :
#             print('.', end='')
#         else:
#             print(abs(h-col), end='')
#     print()


#
# for row in range(1, h+1):
#     for col in range(h*2+1):
#         if row * 2 <= col + row <= h * 2:
#             print('.', end='')
#         else:
#             print(abs(h-col), end='')
#     print()
