
# На вход подаётся строка — это экспоненциальная форма числа.
# Напишите программу, которая выводит отдельно мантиссу и отдельно порядок этого числа.

mantissa = 0
order = 0

num = input('Введите экспоненциальную форму числа: ')

for i in num:
    if i != 'e':
        mantissa = mantissa * 10 + int(i)
    else:
        break
print('mantissa = ', mantissa)

order_len = len(num) - len(str(mantissa)) - 1

for i in range(order_len, 0, -1):
    order = order * 10 + int(num[-i])

print('order = ', order)





