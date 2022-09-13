
template = input('ведите шаблон поздравления, '
                 'в шаблоне можно использовать конструкцию {name} и {age}: ')

name_list = input('Список людей через запятую: ').split(', ')
age_list = input('Возраст людей через пробел: ').split()

print(name_list)

for name in range(len(name_list)):
    print(template.format(name = name_list[name], age = age_list[name]))

people = [' '.join([name_list[i], age_list[i]])
    for i in range(len(name_list))
]

print(', '.join(people))