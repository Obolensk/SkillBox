# TODO здесь писать код

# N = int(input('Кол-во человек: '))
# K = int(input('Какое число в считалке? '))
N = 5
K = 7

print('Значит, выбывает каждый ', K,'-й человек')

list = []
count = 0

for i in range(N):
    list.append(i+1)

while len(list) > 1:
    a = 0
    print()
    print('Текущий круг людей: ', list)
    rem = K % len(list)
    if len(list) == N:
        print('Начало счёта с номера', list[a])
        # if N > K:
        #     rem = N % K
        #     print('Выбывает человек под номером ', list[rem-1])
        # else:
        print('Выбывает человек под номером ', list[rem-1])
        list.pop(rem-1)
        a = rem
    else:
        print('Начало счёта с номера', list[a+1])
        # if N > K:
        #     rem = N % K
        #     print('Выбывает человек под номером ', list[rem-1])
        # else:
        print('Выбывает человек под номером ', list[rem])
        x = list.index(list[rem])
        print('x', x)
        print('a', a)
        list.pop(rem)
        a = rem




print()
print('Остался человек под номером', list[0])
