
string_1 = 'О Дивный Новый мир!'
string_2 = [100, 200, 300, 'буква', 0, 2, 'а']

def uni(my_object):
    new_list = list()
    for item in enumerate(my_object):
        if item[0] % 2 == 0:
            new_list.append(item[1])
    print(new_list)

uni(string_1)
uni(string_2)
