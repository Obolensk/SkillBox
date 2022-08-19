# TODO здесь писать код

people_cnt = int(input('Кол-во человек: '))
drop_number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', drop_number, 'человек')

people_list = []
for i_num in range(1, people_cnt + 1):
    people_list.append(i_num)
index_del = 0

while len(people_list) > 1:
    print('Текущий круг людей:', people_list)
    index_start = index_del % len(people_list)
    print('Начало счёта с номера', people_list[index_start])
    index_del = (index_start + drop_number - 1) % len(people_list)
    print('Выбывает человек под номером', people_list[index_del])
    people_list.remove(people_list[index_del])

print('\nОстался человек под номером', people_list[0])