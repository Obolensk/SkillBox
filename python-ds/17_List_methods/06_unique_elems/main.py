# TODO здесь писать код

first_list = []
second_list = []
for i in range(3):
    print('Введите ', i + 1, end='')
    num = int(input('-е число для первого списка: '))
    first_list.append(num)

for i in range(7):
    print('Введите ', i + 1, end='')
    num = int(input('-е число для второго списка: '))
    second_list.append(num)

print('Первый список: ', first_list)
print('Второй список: ', second_list)

first_list.extend(second_list)

print('Новый первый список с уникальными элементами: ', list(set(first_list)))

# for i in first_list:
#     second_list.remove(i)
#
# for i in second_list:
#     first_list.remove(i)
#
# print(first_list)
# print(second_list)
#
# first_list.extend(second_list)
# print(first_list)