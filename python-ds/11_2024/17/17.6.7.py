# 17.6.7


total = 0
N = int(input('Кол-во коньков: '))
skates = []

for i in range(N):
    print('Размер', i + 1, '-й пары:', end=' ')
    skate = int(input())
    skates.append(skate)

K = int(input('Кол-во людей: '))
foots = []

for i in range(K):
    print('Размер ноги', i, '-го человека:', end=' ')
    foot = int(input())
    foots.append(foot)

for skate in skates:
    for foot in foots:
        if foot == skate:
            total += 1
            break

print('Наибольшее кол-во людей, которые могут взять ролики: ', total)