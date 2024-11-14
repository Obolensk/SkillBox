
num = int(input('Кол-во сотрудников: '))
sal_list = []

for i in range(num):
    print('Зарплата', i, 'сотрудника: ', end='')
    salary = int(input())
    sal_list.append(salary)

print(sal_list)

for i in sal_list:
    if i == 0:
        sal_list.remove(i)

print('\nОсталось сотрудников:', len(sal_list))
print(sal_list)
