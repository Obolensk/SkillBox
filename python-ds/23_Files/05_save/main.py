# TODO здесь писать код

import os

text = input('Введите строку: ')
path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
title = input('Введите имя файла: ')

# Создаю файл
new_title = os.path.join('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/'
                         + path.split()[0] + '/' + path.split()[1] + '/' + title + '.txt')

if os.path.exists(new_title):
    ans = input('Файл существует!!! Вы действительно хотите перезаписать файл? ')
    if ans == 'да' or ans == 'Да':
        # Открываю файл и записываю в него текст
        new_file = open(new_title, 'w+', encoding='utf-8')
        new_file.write(text)
    else:
        print('ГОТОВО!!!')
else:
    # Создаю директорию
    os.makedirs(os.path.join('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/', path.split()[0], path.split()[1]))

    # Открываю файл и записываю в него текст
    new_file = open(new_title, 'w', encoding='utf-8')
    new_file.write(text)

