import os


print(os.listdir('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/'))

for dirs in os.listdir('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/'):
    print()
    print(dirs)
    print(os.path.abspath(dirs))
    # print(os.path.join('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/', os.path.sep, dirs))
    if os.path.exists(os.path.abspath(dirs)):
        if os.path.isfile(os.path.abspath(dirs)):
            print('   Это файл')
        else:
            print('   Скорее всего это уже папка')
    else:
        print('Указанного пути не существует')
