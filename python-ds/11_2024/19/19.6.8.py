
str_1 = 'abcd'
str_2 = 'cdab'
new_str_1 = []
new_str_2 = []
list = []

print(str_1[1])

for i in str_1:
    new_str_1.append(i)

for i in str_2:
    new_str_2.append(i)

print(new_str_1)
print(new_str_2)
print()
# a = 1
#
# for i in range(len(new_str_1)):
#     list.append(new_str_1[(i + a)%len(new_str_1)])

print(list)
print('\nНачинаем вложенные циклы!')
for shift in range(len(new_str_1)):
    for i in range(len(new_str_1)):
        list.append(new_str_1[(i + shift) % len(new_str_1)])
        print(list)
    if list == new_str_1:
        print('Первая строка получается из второй со сдвигом', shift)
        break















#
# shift = int(input('Сдвиг: '))
# start_list = [1, 4, -3, 0, 10]
# fin_list = []
# print('Изначальный список:', start_list)
#
# for i in range(shift, 0, -1):
#     fin_list.append(start_list[-i])
#
# for i in range(len(start_list)-shift):
#     fin_list.append(start_list[i])
# print('Сдвинутый список:', fin_list)