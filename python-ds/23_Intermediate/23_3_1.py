file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/group_1.txt', 'r', encoding='utf-8')
file_2 = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/group_2.txt', 'r', encoding='utf-8')
data = file.read()
print(data)




file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/group_1.txt', 'r', encoding='utf-8')

summa = 0

for i_line in file:
    info = i_line.split()
    summa += int(info[2])

print(summa)

file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/group_1.txt', 'r', encoding='utf-8')

diff = 0

for i_line in file:
    info = i_line.split()
    diff -= int(info[2])

file_2 = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/group_2.txt', 'r', encoding='utf-8')

compose = 1

for i_line in file_2:
    print('i_line = ', i_line)
    print()
    info = i_line.split()
    print('info = ', info)
    compose *= int(info[2])

print()
print('сумму очков первой группы', summa)
print()
print('разность очков опять же первой группы', diff)
print()
print('произведение очков уже второй группы', compose)




















#
# new_file = file.read()
# new_file_2 = file_2.read()
# print('new_file = ', new_file.split())
# print('new_file_2 = ', new_file_2.split())
# summa = 0
#
# for i in new_file.split():
#     if type(i) == int:
#         print(i)
#     else:
#         print(i, ' - это не число')
# # print('file = ', file)
#
# # print(new_file[0])
# # print(file[0])
#
# # for i_line in new_file:
# #     print('i_line = ', i_line)
# #     info = i_line.split()
# #     print(info)
# #
# #
# #     summa += int(info[0])
# #
# # file = open('C:/Users/ASUS/Desktop/my/PYTHON/SkillBox/python-ds/23_Intermediate/group_1.txt', 'r', encoding='utf-8')
# #
# # diff = 0
# #
# # for i_line in file:
# #     info = i_line.split()
# #     # print(info)
# #
# #     diff -= info[2]
# #
# # file_2 = open('C:/Users/ASUS/Desktop/my/PYTHON/SkillBox/python-ds/23_Intermediate/group_2.txt', 'r', encoding='utf-8')
# #
# # compose = 0
# #
# # for i_line in file:
# #     info = i_line.split()
# #
# #     compose *= info[2]
# #
# # print(summa)
# #
# # print(diff)
# #
# # print(compose)
