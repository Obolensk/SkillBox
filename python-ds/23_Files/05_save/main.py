# TODO здесь писать код

import os

text = input('Введите строку: ')
path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
my_path = 'C:/Users/e.menshaev/Desktop/Skillbox/python-ds/' + path.split()[0] + '/' + path.split()[1] + '/'
# dirs_list = dirs.split()
# title = input('Введите имя файла: ')


# new_file.write(text)

text = text + '.txt'
print(text)
print(my_path)
print(my_path + text)

# new_file = open(text, r, encoding='UTF-8')
