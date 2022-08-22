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

s = 0
print('Начало счёта с номера', list[0])
print()


print()
print('ИТЕРАЦИЯ 1 ')
print()


for i in range(s+1, K+1):
    if i % (len(list)+1) == 0 and i != 0:
        s = i % (len(list)+1)
    print('i = счет =', i)
    print('s = индекс = ', s)
    if i % 7 == 0 and i != 0:
        print('Выбывает человек под номером', list[s])
        print()
        list.pop(s)
        print('Текущий круг людей: ', list)
        print('s = ', s, 'list[s] =', list[s])
        if s == list[len(list)-1]:
            print('Начало счёта с номера', list[0])
        else:
            print('Начало счёта с номера', list[s])
    print()
    s += 1
print(s)

print()
print('ИТЕРАЦИЯ 2 ')
print()


for i in range(s-1, K+1):
    if i % (len(list)+1) == 0 and i != 0:
        s = i % (len(list) - i - 2)
    print('i = счет =', i)
    print('s = индекс = ', s)
    if i % 7 == 0 and i != 0:
        print('Выбывает человек под номером', list[s])
        print()
        list.pop(s)
        print('Текущий круг людей: ', list)
        print('s = ', s, 'list[s] =', list[s])
        if s == list[len(list)-1]:
            print('Начало счёта с номера', list[0])
        else:
            print('Начало счёта с номера', list[s])
    print()
    s += 1
print(s)


print()
print('ИТЕРАЦИЯ 3 ')
print()

for i in range(s+1, K+1):
    if i % (len(list)+1) == 0 and i != 0:
        s = i % (len(list)+1)
    print('i = счет =', i)
    print('s = индекс = ', s)
    if i % 7 == 0 and i != 0:
        print('Выбывает человек под номером', list[s])
        print()
        list.pop(s)
        print('Текущий круг людей: ', list)
        print('s = ', s, 'list[s] =', list[s])
        if s == list[len(list)-1]:
            print('Начало счёта с номера', list[0])
        else:
            print('Начало счёта с номера', list[s])
    print()
    s += 1
print(s)