
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]


# Списал решение из разбора преподавателя:

new_new_list = [first for second in nice_list for third in second for first in third]
print('new_new_list = ', new_new_list)


# А это мое решение:

new_list = [((third for third in second) for second in first) for first in nice_list]
print('\nОтвет: ', end='')
for i in new_list:
    for a in i:
        for b in a:
            print(b, end=', ')


