import os
import random

my_dir = 'C:/Users/e.menshaev/PycharmProjects/SkillBox/python-ds'
print(os.listdir(my_dir))
files_list = list()

def list_dir(folder_name):
    for elem in os.listdir(folder_name):
        # print(elem)
        if elem == 'main.py':
            # print('НАШЁЛ!!! Вот он где спрятался - ', os.path.join(folder_name, elem))
            files_list.append(os.path.join(folder_name, elem))
        elif os.path.isdir(os.path.join(folder_name, elem)):
            # print(elem, 'Это папка и вот её содержимое:')
            list_dir(os.path.join(folder_name, elem))
    return files_list



my_list = list_dir(my_dir)
print(my_list)
print(len(my_list))

rand = random.randint(0, len(my_list))
print('\n', my_list[rand])
print()

file = open(my_list[rand], 'r', encoding='utf-8')
print(file.read())