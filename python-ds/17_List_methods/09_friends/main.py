# TODO здесь писать код

list = []
N = int(input('Кол-во друзей: '))

for i in range(N):
    list.append(0)
print(list)

K = int(input('Долговых расписок: '))

for i in range(K):
    print()
    print(i+1, '-я расписка')
    whom = int(input('Кому: '))
    fro = int(input('От кого: '))
    sum = int(input('Сколько: '))
    list[whom-1] -= sum
    list[fro-1] += sum

# print(list)
print('Баланс друзей:')
for i in range(N):
    print(i+1, ':', list[i])