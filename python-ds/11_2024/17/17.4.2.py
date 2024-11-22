
n = int(input('Кол-во участников: '))
k = int(input('Кол-во человек в команде: '))

total = []
player = 1

if n % k == 0:
    for i in range(1, (int(n / k) + 1)):
        team = []
        for _ in range(k):
            team.append(player)
            player += 1
        total.append(team)
    print(total)
else:
    print('{} участников невозможно поделить на команды по {} человек!'.format(n, k))