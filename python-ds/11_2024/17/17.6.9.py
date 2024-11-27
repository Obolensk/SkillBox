# ГОТОВО

# 17.6.9


N = int(input('Кол-во друзей: '))
K = int(input('Долговых расписок: '))
balance = []

for _ in range(N):
    balance.append(0)

# print(balance)

for i in range(K):
    print('\n', i + 1, end='')
    print('-я расписка')
    to = int(input('Кому: '))
    from_ = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    balance[to - 1] += how_much
    balance[from_ - 1] -= how_much

print('\nБаланс друзей: ')
for i in range(N):
    print(i + 1, ':', balance[i])