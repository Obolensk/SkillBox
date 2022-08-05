# TODO здесь писать код
def reverse(n):
    my_list = []
    while n > 0:
        a = n % 10
        my_list.append(int(a))
        n = n // 10
    new_list = ''.join(map(str, my_list))
    return(float(new_list))


N = float(input('Введите первое число: '))
K = float(input('Введите второе число: '))

round_N = N // 1
rem_N = float((N - round_N) * 100 // 1)
round_K = K // 1
rem_K = float((K - round_K) * 100 // 1)
# print(round_N)
# print(round_K)
# print(rem_N)
# print(rem_K)
# print()
# print(reverse(round_N))
# print(reverse(round_K))
# print()
# print(reverse(rem_N)/100)
# print(reverse(rem_K)/100)
# print()
print('Первое число наоборот:', (reverse(round_N) + reverse(rem_N)/100))
print('Второе число наоборот:', (reverse(round_K) + reverse(rem_K)/100))
print('Сумма:', (reverse(round_N) + reverse(rem_N)/100) + (reverse(round_K) + reverse(rem_K)/100))
# print(reverse(rem_N)/100)
# print(reverse(rem_K)/100)

# new_N = float(reverse(round_N)) + float(reverse(rem_N) / 100)
# new_K = float(reverse(round_K)) + float(reverse(rem_K) / 100)
# print(new_N)
# print(new_K)
