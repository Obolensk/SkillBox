# TODO здесь писать код
import calendar

N = 5
# K = int(input('Какое число в считалке? '))
K = 7
print('Значит, выбывает каждый', K, '-й человек')
list = []

for i in range(N):
    list.append(i+1)

print('Текущий круг людей:', list)

s = 1
print('Начало счёта с номера', list[0])
print()

for i in range(list.index(s), K+1):
    if i % len(list) == 0 and i != 0:
        s = i % len(list)
    print('i = индекс =', i)
    print('s = значение = ', s)
    if i % 7 == 0 and i != 0:
        print('Выбывает человек под номером', list[s-1])
        print()
        list.pop(s-1)
        print('Текущий круг людей: ', list)
        if list[s-1] == list[len(list)-1]:
            print('Начало счёта с номера', list[0])
        else:
            print('Начало счёта с номера', list[s-1])
    print()
    s += 1
print(s)

print()


for i in range(list.index(s), K+1):
    if (i+1) % len(list) == 0 and i != 0:
        s = (i+1) % len(list)
    print('i = индекс =', i)
    print('s = значение = ', s)
    if i % 7 == 0 and i != 0:
        print('Выбывает человек под номером', list[s-1])
        print()
        list.pop(s-1)
        print('Текущий круг людей: ', list)
        if list[s-1] == list[len(list)-1]:
            print('Начало счёта с номера', list[0])
        else:
            print('Начало счёта с номера', list[s-1])
    print()
    s += 1
print(s)

print()


for i in range(list.index(s), K+1):
    if (i+1) % len(list) == 0 and i != 0:
        s = (i+1) % len(list)
    print('i = индекс = ', i)
    print('s = значение = ', s)
    if i % 7 == 0 and i != 0:
        print('Выбывает человек под номером', list[s-1])
        print()
        list.pop(s-1)
        print('Текущий круг людей: ', list)
        if list[s-1] == list[len(list)-1]:
            print('Начало счёта с номера', list[0])
        else:
            print('Начало счёта с номера', list[s-1])
    print()
    s += 1
print(s)


# 1. Сформировать список +
# 2. Цикл начиная с элемента (0) идем по каждому i-тому элементу списка
# 3. Если i == len(list) то i = 0 (бесконечный цикл или пока len(list) != 1)
# 4. добавить в цикл счетчик х, если х % 7 == 0, то list.pop(i)
# 5. Начинаем с элемента list[i] (после удаления)
# 6.
# 7.
# 8.
# 9.
# 10.
# 11.
# 12.
# 13.
# 14.
# 15.






#
# while len(list) != 1:
#     # print(i)
#     # print(s)
#     for i in range(len(list)-3):
#
#         print()
#         print('1_Текущий круг людей:', list)
#         print('1_Начало счёта с номера', list[i])
#         print('i до удаления', i)
#         for a in range(K):
#             s = a
#             if a >= len(list):  # len(list)
#                 s = a - len(list)
#             s += 1
#             print(s)
#
#         print('1_Выбывает человек под номером', list[i])
#         list.pop(i)
#         print('i после удаления', i)
#         print('2_Начало счёта с номера', list[i])
#


