first = ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
second = ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']

def make_dict(my_list):
    my_dict = dict()
    for item in enumerate(my_list):
        my_dict[item[0]] = item[1]
    return my_dict

print('Первый словарь:', make_dict(first))
print('Второй словарь:', make_dict(second))
