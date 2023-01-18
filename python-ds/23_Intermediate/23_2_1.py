import os


print(os.listdir('C:/Users/e.menshaev/Desktop'))
# print(os.path.isdir('C:\Program Files'))
# print(os.path.isfile('C:\Program Files'))
mypath = os.path.abspath('C:/Users/e.menshaev/Desktop')
print()

for fold in os.listdir(mypath):
    print(fold)
    print(os.path.join(mypath, os.path.sep, fold))
    print('os.path.isfile(fold) = ', os.path.isfile(os.path.join(mypath, os.path.sep, fold)))
    print('os.path.isdir(fold) = ', os.path.isdir(os.path.join(mypath, os.path.sep, fold)))
    print('os.path.exists(fold) = ', os.path.exists(os.path.join(mypath, os.path.sep, fold)))
    if os.path.isfile(os.path.join('C:/Users/e.menshaev/Desktop', os.path.sep, fold)):
        print(os.path.join('C:/Users/e.menshaev/Desktop', os.path.sep, fold), end=' - ')
        print('Это файл')
    else:
        # print('os.path.isfile(os.path.join(fold)', os.path.isfile(os.path.join('C:', os.path.sep, fold)))
        # print('os.path.isdir(os.path.join(fold)', os.path.isdir(os.path.join('C:', os.path.sep, fold)))
        print(os.path.join('C:/Users/e.menshaev/Desktop', os.path.sep, fold), end=' - ')
        print('Это папка')
        # print('Вот её содержимое:')
        # print(os.listdir(os.path.join('C:', os.path.sep, fold)))
        # print()
