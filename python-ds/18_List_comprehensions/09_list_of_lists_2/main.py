nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# TODO здесь писать код

new_list = [list_1 for list_2 in nice_list for list_3 in list_2 for list_1 in list_3]

print('nice_list = ', nice_list)
print('new_list = ', new_list)

# new = []
# for i in nice_list:
#     for n in i:
#         for a in n:
#             new.append(a)

