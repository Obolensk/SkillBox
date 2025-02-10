
country_1 = 'Россия Москва Петербург Новгород'
country_2 = 'Германия Берлин Лейпциг Мюнхен'
country_dict = dict()


def get_country_info(country):
    country_dict[country.split()[0]] = list()
    for i in range(1, len(country.split())):
        country_dict[country.split()[0]].append(country.split()[i])
    return country_dict

get_country_info(country_1)
get_country_info(country_2)

city_1 = 'Москва'
city_2 = 'Мюнхен'
city_3 = 'Рим'

def get_city_info(city):
    count = 0
    for country in country_dict:
        if city in country_dict[country]:
            print('Город {} расположен в стране {}.'.format(city, country))
            count += 1
            break
    if count == 0:
        print('По городу {} данных нет.'.format(city))

get_city_info(city_1)
get_city_info(city_2)
get_city_info(city_3)
