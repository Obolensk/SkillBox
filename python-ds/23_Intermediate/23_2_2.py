import os

my_dir = 'C:/Users/e.menshaev/Desktop/Skillbox/python-ds/15_IDE/'
file_name = 'main.py'

for dirs in os.listdir(my_dir):
    print()
    print(dirs)
    for file in os.listdir(os.path.join(my_dir, dirs)):
        print('   ', file)
        if file == file_name:
            print('   ', os.path.join(my_dir, dirs, file), end=' - ')
            print('Размер файла -', os.path.getsize(os.path.join(my_dir, dirs, file)), 'байт!')


