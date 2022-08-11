my_list = []
index_sum = 0
N = int(input('Кол-во чисел в списке: '))
for i in range(N):
    print('Введите', i+1, end=' ')
    a = int(input('число: '))
    my_list.append(a)

print()
K = int(input('Введите делитель: '))
print()

for i in range(len(my_list)):
    if my_list[i] % K == 0:
        print('Индекс числа', my_list[i], ':', i)
        index_sum += i

print('Сумма индексов:', index_sum)
