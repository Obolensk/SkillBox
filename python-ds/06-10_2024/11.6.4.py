num = int(input('Введите количество чисел: '))
answer = 0
while num > 0:
    n = int(input('Введите число: '))
    wrong = 0
    for i in range(2, n):
        if n % i == 0:
            wrong += 1
    if wrong == 0:
        answer += 1
    num -= 1
print('Количество простых чисел в последовательности равно', answer)