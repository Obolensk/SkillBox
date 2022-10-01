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

family_member = {
  "name": "Jane",
  "surname": "Doe",
  "hobbies": ["running", "sky diving", "singing"],
  "age": 35,
  "children": [{
    "name": "Alice",
    "age": 6
  }, {
    "name": "Bob",
    "age": 8
  }]
}

# print(family_member)

i_name = input('Введите имя ребенка: ')

# print(family_member.get('children')[0])

kid_count = 0
for i in family_member.get('children'):
  if i['name'] == i_name:
    print('Ребенок с именем {0} у {1} есть'.format(i_name,
                                                   family_member['name']))
    kid_count += 1
    break

if kid_count == 0:
  print('Ребенка с именем {0} у {1} нет'.format(i_name, family_member['name']))
