
employees = []
num = int(input('Кол-во сотрудников в офисе: '))
for i in range(num):
    i = int(input('ID сотрудника: '))
    employees.append(i)

ident = int(input('Какой ID ищем? '))
if ident in employees:
    print('Сотрудник в офисе')
else:
    print('Сотрудник не работает!')