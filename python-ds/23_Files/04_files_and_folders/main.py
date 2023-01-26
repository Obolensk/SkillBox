# TODO здесь писать код

import os
files = 0
folders = 0
size = 0


# print('1 = ', os.listdir('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/'))

for dirs in os.listdir('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/'):
    # print()
    # print('2 = ', dirs)
    # print('3 = ', os.path.abspath(dirs))
    # print('os.path.isfile(os.path.abspath(dirs)) =', os.path.isfile(os.path.join('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/', dirs)))
    if os.path.isfile(os.path.join('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/', dirs)):
        # print('   Это файл')
        files += 1
        size += os.path.getsize(os.path.join('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/', dirs))
    else:
        # print('   Скорее всего это уже папка')
        folders += 1
        size += os.path.getsize(os.path.join('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/', dirs))

print('Количество файлов:', files)
print('Количество подкаталогов:', folders)
print('Размер каталога (в Кб):', size / 1024, 'Кб')