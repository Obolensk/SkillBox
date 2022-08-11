
emp_num = int(input('Кол-во сотрудников: '))
sal_list = []
for i in range(emp_num):
    print('Зарплата', i, end=' ')
    sal = int(input('сотрудника: '))
    if sal > 0:
        sal_list.append(sal)
print('Осталось сотрудников: ', len(sal_list))
print('Зарплаты: ', sal_list)
