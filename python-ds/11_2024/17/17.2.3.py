
film_list = []

while True:
    print('\nВаш текущий топ фильмов:', film_list)
    film = input('Название фильма: ')
    print('Команды: добавить, вставить, удалить')
    command = input('Введите команду: ')
    if command == 'добавить':
        film_list.append(film)
    elif command == 'вставить':
        film_list.insert(0, film)
    elif command == 'удалить':
        film_list.remove(film)





