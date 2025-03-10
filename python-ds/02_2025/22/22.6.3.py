# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))


def fibo_func(fibo_len):
    fibo = [1, 1]
    for i in range(1, fibo_len):
        fibo.append(fibo[i] + fibo[i-1])
    return fibo[fibo_len]


print(fibo_func(num_pos-1))


