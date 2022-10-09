# TODO здесь писать код


all_dict = {
    'Россия': ['Москва', 'Петербург', 'Новгород'],
    'Германия': ['Берлин', 'Лейпциг', 'Мюнхен']
}

# print(all_dict)
# print(all_dict.values)
# print(all_dict.keys())
# print(all_dict.items())
# print(all_dict.get('Россия'))



for i in range(3):
    print(i + 1, 'город', end = '')
    city = input(' ')
    for country in all_dict.keys():
      if city in all_dict.get(country):
        print('Город {0} расположен в стране {1}'.format(city, country))
        break
      else:
        print('По городу {0} данных нет'.format(city))
        break


