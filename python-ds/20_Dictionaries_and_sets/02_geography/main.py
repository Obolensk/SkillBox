# TODO здесь писать код

# country_num = int(input('Кол-во стран: '))
#
# country_dict = dict()
# all_dict = dict()
#
# for country in range(country_num):
#     print(country + 1, 'страна', end = '')
#     name = input(' ')
#     country_info = name.split()
#     country_dict[country_info[0]] = country_info[1:4]
#     all_dict.update(country_dict)
# print(all_dict)
# print(all_dict.values())
# print(all_dict.keys())
# print(all_dict.items())
# print(all_dict.get('sf'))
#

all_dict = {
    'Россия': ['Москва', 'Петербург', 'Новгород'],
    'Германия': ['Берлин', 'Лейпциг', 'Мюнхен']
}

print(all_dict)

for i in range(3):
    print(i + 1, 'город', end = '')
    city = input(' ')
    for _ in range(len(all_dict)):
        for _ in range(3):
            if city in all_dict.values():
                print(all_dict.keys())
