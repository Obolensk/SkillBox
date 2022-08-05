# TODO здесь писать код

all_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day = []
for i in range(len(all_list)):
    if i % 2 == 0:
        first_day.append(all_list[i])
print('Первый день:', first_day)