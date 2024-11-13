#
# # shift = int(input('Сдвиг: '))
# shift = 3
#
# first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# second_list = []
#
# # for i in range(shift + 1, 0, -1):
# #     second_list.append(first_list[-i])
#
# for i in range(len(first_list)-shift):
#     second_list.append(first_list[i + shift])
#
# print(second_list)



# 16.5.8

# shift = 3
shift = int(input('Сдвиг: '))
start_list = [1, 4, -3, 0, 10]
fin_list = []
print('Изначальный список:', start_list)

for i in range(shift, 0, -1):
    fin_list.append(start_list[-i])

for i in range(len(start_list)-shift):
    fin_list.append(start_list[i])
print('Сдвинутый список:', fin_list)