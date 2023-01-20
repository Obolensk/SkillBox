import os
import random

my_dir = 'C:/Users/e.menshaev/Desktop/Skillbox/python-ds/15_IDE/'
file_name = 'main.py'
count = random.randint(2, 4)
print(count)
i = 0

for dirs in os.listdir(my_dir):
    print()
    print(dirs)
    for file in os.listdir(os.path.join(my_dir, dirs)):
        print('   ', file)
        if file == file_name:
            print('   ', os.path.join(my_dir, dirs, file), end=' - ')
            print('Размер файла -', os.path.getsize(os.path.join(my_dir, dirs, file)), 'байт!')
            my_read = open(os.path.join(my_dir, dirs, file), 'r', encoding= 'UTF-8')
            i += 1
            if count == i:
                my = my_read.read()
                print(my)
                print()
        else:
            continue

