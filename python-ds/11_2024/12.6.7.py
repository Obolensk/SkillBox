print('Введите местоположение коня: ')
k_x = -1
k_y = -1
p_x = -1
p_y = -1

while k_x < 0 or k_x > 0.8:
    print()
    print('Координаты должны быть в диапазоне от 0 до 8')
    k_x = float(input('Введите координаты k_x: '))

while k_y < 0 or k_y > 0.8:
    print()
    print('Координаты должны быть в диапазоне от 0 до 8')
    k_y = float(input('Введите координаты k_y: '))

print('Введите местоположение точки на доске: ')

while p_x < 0 or p_x > 0.8:
    print()
    print('Координаты должны быть в диапазоне от 0 до 8')
    p_x = float(input('Введите координаты p_x: '))

while p_y < 0 or p_y > 0.8:
    print()
    print('Координаты должны быть в диапазоне от 0 до 8')
    p_y = float(input('Введите координаты p_y: '))

knight_x = int(k_x * 10)
knight_y = int(k_y * 10)
point_x = int(p_x * 10)
point_y = int(p_y * 10)

print('Конь в клетке ({}, {})'.format(knight_x, knight_y))
print('Точка в клетке ({}, {})'.format(point_x, point_y))

if ((abs(knight_x - point_x) == 2 and abs(knight_y - point_y) == 1) or
        (abs(knight_x - point_x) == 1 and abs(knight_y - point_y) == 2)):
    print('Да, конь может ходить в эту клетку!')
else:
    print('Нет, конь в эту клетку ходить не может!')