# Почти получилось, потестить с точкой останова!


# 17.6.8

game = []
first_count = 0

N = int(input('Кол-во человек: '))
K = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', K, '-й человек')

for i in range(N):
    game.append(i + 1)

while len(game) != 1:
    print('============================================')
    print()
    print(' === first_count =', first_count, ' === ')
    print(' === len(game) =', len(game), ' === ')
    print('\nТекущий круг людей:', game)
    print('Начало счёта с номера:', game[first_count % len(game)])

    # print('Выбывает человек под номером:', game[(first_count + K)%len(game)-1])
    # game.remove(game[(first_count + K)%len(game)-1])
    # first_count = game[(first_count + K - 2)]

    print('Выбывает человек под номером:', game[(first_count + K - 1) % len(game)])
    game.remove(game[(first_count + K - 1) % len(game)])
    first_count = game.index(game[(first_count + K - 2) % len(game)])
    # first_count += abs(K - 1)

print('\nОстался человек под номером', game[0])