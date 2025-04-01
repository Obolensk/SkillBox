file = open('group_1.txt', 'r', encoding='utf-8')
summa = 0

for i_line in file:
    info = i_line.split()
    print(info)
    summa += int(info[2])
file.close()

print(summa)
#
file = open('group_1.txt', 'r', encoding='utf-8')
diff = 0
#
for i_line in file:
    info = i_line.split()
    print(info)
    diff -= int(info[2])
file.close()

print(diff)
#
file_2 = open(
    'C:/Users/e.menshaev/PycharmProjects/SkillBox/python-ds/03_2025/23/23_3_1/task/Additional_info/group_2.txt',
    'r',
    encoding='utf-8')
compose = 1

for i_line in file_2:
    info = i_line.split()
    print(info)
    compose *= int(info[2])

print(summa)
print(diff)
print(compose)


