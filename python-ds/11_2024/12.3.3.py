print('Введите расположение фигуры!')
hor = -1
ver = -1
while hor > 1 or hor < 0:
    hor = float(input('По горизонтали (от нуля до единицы): '))
while ver > 1 or ver < 0:
    ver = float(input('По вертикали (от нуля до единицы): '))
S_hor = int(hor*10)
S_ver = int(ver*10)
hor_centr = S_hor + 0.5
print('hor_centr = ', hor_centr)
ver_centr = S_ver + 0.5
print('ver_centr = ', ver_centr)
print()
print('Фигура находится в клетке ' + '(' + str(S_hor) + ',' + str(S_ver) + ')')
print('Поправьте положение фигуры на ({},{})'.format(round(hor_centr/10 - hor, 3), round(ver_centr/10 - ver, 3)))
