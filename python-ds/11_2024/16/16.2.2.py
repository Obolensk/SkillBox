
N = int(input('Кол-во чисел в списке: '))
num_list = []
answer = 0

for i in range(1, N + 1):
    print('Введите', i, 'число: ', end='')
    a = int(input())
    num_list.append(a)

print(num_list)

K = int(input('Введите делитель: '))

for i in range(len(num_list)):
    if num_list[i] % K == 0:
        answer += i
        print('Индекс числа {}: {}'.format(num_list[i], i))

print('Сумма индексов:', answer)

