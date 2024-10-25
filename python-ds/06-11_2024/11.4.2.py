n = int(input('Сколько чисел в последовательности? '))
my_list = []
count = 1
answer = 0
while count <= n:
    print('Введите {}-e число последовательности: '.format(count), end='')
    num = int(input())
    my_list.append(num)
    count += 1
    while num > 5:
        if num % 10 > 5:
            answer += 1
        num //= 10

print('Количество цифр больше пяти в последовательности чисел {}, равно {}'.format(my_list, answer))


