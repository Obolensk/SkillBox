films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# TODO здесь писать код

my_films_nums = int(input('Сколько фильмов хотите добавить? '))
fav_films = []
for i in range(my_films_nums):
    my_film = input('Введите название фильма: ')
    if my_film in films:
        fav_films.append(my_film)
    else:
        print('Ошибка: фильма', my_film, 'у нас нет :(')

print('Ваш список любимых фильмов:', fav_films)