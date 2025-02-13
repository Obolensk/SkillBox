n = int(input('Введите количество человек: '))
global_dict = dict()

for pair in range(n-1):
    print(pair+1, end=' ')
    couple = input('пара: ')
    if pair == 0:
        global_dict[couple.split()[0]] = 1
        global_dict[couple.split()[1]] = 0
    elif couple.split()[1] in global_dict:
        global_dict[couple.split()[0]] = global_dict[couple.split()[1]] + 1

print()
print('“Высота” каждого члена семьи:')
for i in sorted(global_dict):
    print(i, global_dict[i])

