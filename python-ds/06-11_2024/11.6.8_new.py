# h = int(input('Введите число: '))
h = 5

for row in range(1, h+1):
    for col in range(h*2+1):
        if row * 2 <= col + row <= h * 2:
            print('.', end='')
        else:
            print(abs(h-col), end='')
    print()

#
# for row in range(1, h+1):
#     for col in range(h*2+1):
#         if row * 2 <= col + row <= h * 2:
#             print('.', end='')
#         else:
#             print(abs(h-col), end='')
#     print()
