
films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]
my_top = []
while True:
    print('Ваш текущий топ фильмов: ', my_top)
    new_film = input('Название фильма: ')
    if new_film in my_top:
        print('Этот фильм уже есть в вашем списке.')
    else:
        print('Команды: добавить, вставить, удалить')
        command = input('Введите команду: ')
        if command == 'добавить':
            my_top.append(new_film)
        if command == 'вставить':
            ind = int(input('На какое место вставить: '))
            my_top.insert(ind, new_film)
        if command == 'удалить':
            my_top.remove(new_film)