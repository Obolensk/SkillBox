
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
#
# Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

# new_list = [i for i in nice_list]
my_list = []
new = []
w = []

for first in nice_list:
    # print(first)
    for second in first:
        new.extend(second)
        # for third in second:
        #     print(third)
        #     my_list.append(third)

new_list = [((third for third in second) for second in first) for first in nice_list]
print(((third for third in second) for second in first) for first in nice_list)
# new_list =

print('new_list = ', new_list)
print('my_list = ', my_list)
print()
print('\nОтвет: ', end='')
for i in new_list:
    # print(i, end='')
    for a in i:
        for b in a:
            print(b, end=', ')
#
# new_new = [((a for a in b) for b in c) for c in nice_list]
# print('new_new = ', new_new)
print()
print(new)
print()
print(w)

