# TODO здесь писать код

import random

summ = 0

while summ < 777:
    num = int(input('Введите число: '))
    try:
        summ += num
        try_ex = num/random.randint(0, 12)
    except:
        print('Вас постигла неудача!')
        break
    with open('out_file.txt', 'a', encoding='utf-8') as file:
        file.write(str(num))
        file.write('\n')
if summ >= 777:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')



