# 17.6.6


list_1 = []
for i in range(3):
    print('Введите', i + 1, '-е число для первого списка:', end=' ')
    num = int(input())
    list_1.append(num)

list_2 = []
for i in range(7):
    print('Введите', i + 1, '-е число для второго списка:', end=' ')
    num = int(input())
    list_2.append(num)

print('Первый список:', list_1)
print('Второй список:', list_2)

list_1.extend(list_2)
print('Новый первый список с уникальными элементами:', set(list_1))