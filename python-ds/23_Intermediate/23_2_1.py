import os

# print(os.path.join('..', os.getcwd()))
#
# print(os.path.abspath('/'))
# print(os.listdir('/'))

print(os.listdir('C:\Program Files'))
print(os.path.isdir('C:\Program Files'))
print(os.path.isfile('C:\Program Files'))
print()

for fold in os.listdir('C:/Users/e.menshaev/Desktop/Skillbox'):
    # print(fold)
    # print(os.path.join('C:', os.path.sep, fold))
    # print('os.path.isfile(fold) = ', os.path.isfile(os.path.join('C:', os.path.sep, fold)))
    # print('os.path.isdir(fold) = ', os.path.isdir(os.path.join('C:', os.path.sep, fold)))
    # print('os.path.exists(fold) = ', os.path.exists(os.path.join('C:', os.path.sep, fold)))
    if os.path.isfile(os.path.join('C:', os.path.sep, fold)):
        print(os.path.join('C:', os.path.sep, fold))
        print('Это файл')
    else:
        # print('os.path.isfile(os.path.join(fold)', os.path.isfile(os.path.join('C:', os.path.sep, fold)))
        # print('os.path.isdir(os.path.join(fold)', os.path.isdir(os.path.join('C:', os.path.sep, fold)))
        print(os.path.join('C:', os.path.sep, fold))
        print('Это папка')
        print('Вот её содержимое:')
        print(os.listdir(os.path.join('C:', os.path.sep, fold)))
        print()
