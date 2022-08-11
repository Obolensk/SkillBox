# TODO здесь писать код
n = int(input('Введите число: '))
sum = 0
for num in range(len(str(n))):
    num += 1
    sum += n % 10
    n //= 10
print('Сумма цифр:', sum)
print('Кол-во цифр в числе:', num)
print('Разность суммы и кол-ва цифр:', sum - num)
