# h = int(input('Введите число: '))
h = 5
for row in range(1, h+1):
    print()
    for col in range(h*2-row):
        for i in range(row):
            if col == i or col == h * 2 - 1 - i:
                print(h-i, end='')
        else:
            print('.', end='')
    # print()






    #
    #     if col + row >= h - 1:
    #         if row % 2 == 0:
    #             if col % 2 == 0:
    #                 print(num, end='\t')
    #                 num += 2
    #             else:
    #                 print(' ', end='\t')
    #         else:
    #             if col % 2 != 0:
    #                 print(num, end='\t')
    #                 num += 2
    #             else:
    #                 print(' ', end='\t')
    #     else:
    #         print(' ', end='\t')
    # print()

