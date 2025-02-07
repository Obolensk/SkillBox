# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }

family_member = dict()

family_member['name'] = 'Jane'
family_member['surname'] = 'Doe'
family_member['hobbies'] = ["running", "sky diving", "singing"]
family_member['age'] = 35
family_member['children'] = list()
dict_1 = dict()
dict_1['name'] = 'Alice'
dict_1['age'] = 6
family_member['children'].append(dict_1)
dict_2 = dict()
dict_2['name'] = 'Bob'
dict_2['age'] = 8
family_member['children'].append(dict_2)

baby = input('Введите имя ребенка: ')
count = 0


for kids in family_member['children']:
    if baby in kids['name']:
        count += 1
if count == 1:
    print('Ребенок с именем {} есть в семье'.format(baby))
else:
    print('Ребенок с именем {} в семье отсутствует'.format(baby))
count = 0





print(family_member)