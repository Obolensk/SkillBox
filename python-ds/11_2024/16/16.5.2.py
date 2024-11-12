
my_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day = []
second_day = []

for i in range(len(my_list)):
    if i % 2 == 0:
        first_day.append(my_list[i])
    else:
        second_day.append(my_list[i])

print('Первый день:', first_day)
print('Второй день:', second_day)
