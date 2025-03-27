import os

my_dir = 'C:/Users/ASUS/Desktop/SkillBox/python-ds'
print(os.listdir(my_dir))

def list_dir(folder_name):
    for elem in os.listdir(folder_name):
        # print(elem)
        if elem == 'main.py':
            print('НАШЁЛ!!! Вот он где спрятался - ', os.path.join(folder_name, elem))
        elif os.path.isdir(os.path.join(folder_name, elem)):
            # print(elem, 'Это папка и вот её содержимое:')
            list_dir(os.path.join(folder_name, elem))

list_dir(my_dir)