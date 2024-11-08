print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по числу х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

precision = float(input('Введите точность: '))
x = int(input('Введите x: '))
factorial = 1
new_pres = 0
while precision != 1:
    precision *= 10
    new_pres += 1
# print(precision)
# print(new_pres)
sum = 0
for num in range(2, 36, 2):
    # print()
    # print('num =', num)
    # print(x, 'в степени ', num, ' =', pow(x, num))
    for i in range(1, num + 1):
        factorial = factorial * i
    # print("Факториал", num, "равен", factorial)
    # print(x, 'в степени ', num, 'деленое на факториал', num, '=', pow(x, num)/factorial)

    if num == 2:
        # print('с минусом')
        sum += 1 - (1 * pow(x, num) / factorial)
        # print('sum =', sum)
    elif num % 4 == 0:
        # print('с плюсом')
        sum += 1 * pow(x, num) / factorial
        # print('sum =', sum)
    else:
        # print('с минусом')
        sum += -1 * pow(x, num) / factorial
        # print('sum =', sum)
    factorial = 1
print('sum =', sum)
print('sum =', round(sum, new_pres))
