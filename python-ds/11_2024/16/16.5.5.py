
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']

favorite = []

films_num = int(input('Сколько фильмов хотите добавить: '))

while len(favorite) < films_num:
    fav = input('Введите название фильма: ')
    if fav in films:
        favorite.append(fav)
        print('Фильм', fav, 'добавлен в любимые!')
    else:
        print('Ошибка: фильма', fav, 'у нас нет :(')

print('Ваш список любимых фильмов:', favorite)

