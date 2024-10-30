num = int(input('Введите количество чисел: '))
answer = 0
total = 0
while num > 0:
    list = []
    summ = 0
    n = int(input('Введите число: '))
    for i in str(n):
        # print(i)
        summ += int(i)
    if summ > total:
        total = summ
        answer = n
    num -= 1

print('Число содержащее наибольшую сумму цифр - {}, сумма - {}'.format(answer, total))