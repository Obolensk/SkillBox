h = int(input('Введите высоту рамки: '))
w = int(input('Введите ширину рамки: '))

for row in range(h+1):
    if row == 0 or row == h:
        print('|', '-' * (w - 2), '|')
    else:
        print('|', ' ' * (w - 2), '|')