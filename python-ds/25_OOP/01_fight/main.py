# TODO здесь писать код

import random

w1 = 100
w2 = 100

while w1 > 0 and w2 > 0:
    if random.randint(1, 2) == 1:
        print('Воин 1 бьет Воина 2')
        w2 -= 10
        print('У Воина 1 - {} очков'.format(w1))
        print('У Воина 2 - {} очков\n'.format(w2))
    else:
        print('Воин 2 бьет Воина 1')
        w1 -= 10
        print('У Воина 1 - {} очков'.format(w1))
        print('У Воина 2 - {} очков\n'.format(w2))

if w1 > w2:
    print('Победу одержал Воин 1!!!')
else:
    print('Победу одержал Воин 2!!!')