

# TODO здесь писать код
N = 5
# K = int(input('Какое число в считалке? '))
K = 7
print('Значит, выбывает каждый', K, '-й человек')
list = []
# i = 0
s = 0

for i in range(N):
    list.append(i+1)

# print(list)

for i in list:
    for a in range(K):
        s = a
        if a >= len(list):
            s = a - len(list)
        print(list[s])
        s += 1
    print()
    print('1_Выбывает человек под номером', list[s-1])
    list.pop(s-1)
    print(list)
    print('1_Начало счёта с номера', list[s-1])


    # print('1_Выбывает человек под номером', list[s-1]+i)
    # list.remove(list[s-1]+i)
    # print(list)
    # print('1_Начало счёта с номера', list[s-1]+i)
    # print()
