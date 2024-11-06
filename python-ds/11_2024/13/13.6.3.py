
def add(a, b):
    print('Сумма чисел {} и {} равняется {}'.format(a, b, a + b))

def minimum(a, b):
    if a < b:
        print('Число {} меньше {}'.format(a, b))
    else:
        print('Число {} меньше {}'.format(b, a))

def maximum(a, b):
    if a > b:
        print('Число {} больше {}'.format(a, b))
    else:
        print('Число {} больше {}'.format(b, a))

def new_act():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    act = int(input('Введите необходимое действие, 1 - сложить, 2 - минимум, 3 - максимум: '))
    if act == 1:
        add(a, b)
    elif act == 2:
        minimum(a, b)
    else:
        maximum(a, b)
    new_act()

new_act()