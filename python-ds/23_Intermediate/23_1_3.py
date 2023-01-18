import os

print(os.listdir('C:\Program Files'))
print(os.path.isdir('C:\Program Files'))
print(os.path.isfile('C:\Program Files'))
print()
print(os.listdir('/'))
print()

def print_dir(path):
    for fold in os.listdir(path):
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
            print(os.listdir(fold))
            print('Это папка')
            # print_dir(os.path.join('C:', os.path.sep, fold))

print_dir('/')