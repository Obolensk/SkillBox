
def create_dict(data):
    template = {}
    if isinstance(data, dict):
        return data
    elif isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
        template[data] = data
        return template


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        new_list.append(create_dict(i_element))
    print('new_list = ', new_list)
    print('Первая итерация цикла')
    for elem in new_list:
        print('Полный список элементов', elem)
        print(isinstance(elem, dict))
        if not isinstance(elem, dict):
            print('Удаляем элемент', elem)
            print(isinstance(elem, dict))
            new_list.remove(elem)
    print('new_list = ', new_list)
    print('Вторая итерация цикла')
    for elem in new_list:
        print('Полный список элементов', elem)
        print(isinstance(elem, dict))
        if not isinstance(elem, dict):
            print(isinstance(elem, dict))
            print('Удаляем элемент', elem)
            new_list.remove(elem)
    print('new_list = ', new_list)
    return new_list

data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]


print()
for i in data:
    print('\nДля аргумента i = {}, create_dict(i) = {}'.format(i, create_dict(i)))

print()
print(create_dict(7878))
print()
print(data_preparation(data))



