

def avg(a, b):
    if a >= b:
        print('Error!!!')
    else:
        print((a+b)/2)

left = int(input('Введите левую границу: '))
right = int(input('Введите праву границу: '))


avg(left, right)