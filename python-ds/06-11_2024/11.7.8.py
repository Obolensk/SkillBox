num = int(input('Введите число: '))

for col in range(num-1):
    # print('col = ', col, 'num =', num, num-col)
    print(num-col, end='')
    for i in range(col):
        print(col-i, end='')
    #     print(str(num - i), end='')
    #     print(str(num - i - 1), end='')
        print(str('.' * (num-i)), end='')
        print(str('.' * (num-i)), end='')
    #     print(str(num - i - 1), end='')
    #     print(str(num - i))


#
#
# for i in range(num):
#     print(str(num - i) + str('.' * (num-i-1)), end='')
#     # for k in range(i):
#     #     print(i-k-1, '.' * k, i-k-1, end='')
#     print(str('.' * (num-i-1)) + str(num - i))




#
# for row in range(num):
#     for col in range(row):
#         print('row = ', row)
#         print('col = ', col)
#         print(str(num - col) + (str(num - row) * col) + str('.' * ((num - col) * 2 - 2)) + (str(num - row) * col) + str(num - col))
#         print()
# print()
#
# for col in range(num):
#     print(str(num-col) + str('.' * ((num-col) * 2 - 2)) + str(num-col))


print()
print('*********************************************')
print()
print(str(num) + str('.' * (num*2-2)) + str(num))
print(str(num) + str(num-1) + str('.' * (num*2-2-2)) + str(num-1) + str(num))
print(str(num) + str(num-1) + str(num-1-1) + str('.' * (num*2-2-2-2)) + str(num-1-1) + str(num-1) + str(num))
print(str(num) + str(num-1) + str(num-1-1) + str(num-1-1-1) + str('.' * (num*2-2-2-2-2)) + str(num-1-1-1) + str(num-1-1) + str(num-1) + str(num))
print(str(num) + str(num-1) + str(num-1-1) + str(num-1-1-1) + str(num-1-1-1-1) + str('.' * (num*2-2-2-2-2-2)) + str(num-1-1-1-1) + str(num-1-1-1) + str(num-1-1) + str(num-1) + str(num))

