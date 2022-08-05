employee_nums = int(input('Кол-во сотрудников в офисе: '))
employee_list = []
for i in range(employee_nums):
    a = int(input('ID сотрудника: '))
    employee_list.append(a)
find_id = int(input('Какой ID ищем? '))
if find_id in employee_list:
    print('Сотрудник на месте')
else:
    print('Сотрудник не работает!')

# print(employee_list)


