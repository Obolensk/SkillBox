# levels = int(input('Введите количество уровней пирамиды: '))
levels = 5
level = 0
count = 1
#
# for space in range(levels):
#     print(' ' * (levels*2 - space*2 - 2), end='')
#     print(space+1, end='')
#     print(' ')

for row in range(levels):
    for col in range(levels):
        print(' ' * (levels - row - 1), end='')
        print(count, end='')
        print(' ', end='')
        count += 2
    print(count)
    count += 2
#
# Псевдокод
# Есть таблица размером N x N
# На пересечении столбцов и строк какие-то значения
# Допустим размер 5:
# Строки х столбцы:
# 0 х 0 = " "
# ...
# 0 х 8 = 1
# 1 х 6 = 3
# 1 х 10 = 5
# 2 х 4 = 7
# 2 х 8 = 9
# 2 х 12 = 11
# 3 х 2 = 13
# 3 х 6 = 16
# 3 х 10 = 17
# 3 х 14 = 19
# 4 х 0 = 21
# 4 х 4 = 23
# 4 х 8 = 25
# 4 х 12 = 27
# 4 х 16 = 29
#
# Все остальные ячейки таблицы равны " "

