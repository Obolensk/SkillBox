import os

new_file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/scripts.txt', 'a', encoding='UTF-8')
for i in os.listdir('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/15_IDE/07_years'):
    script = open(os.path.join('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/15_IDE/07_years', i), 'r',
                  encoding='UTF-8')
    my_script = script.read()
    print(i)
    print(my_script)
    new_file.write(my_script)
    new_file.write('\n ')
    new_file.write('\n****************************************')
    new_file.write('\n ')





#
# my_dir = 'C:/Users/e.menshaev/Desktop/Skillbox/python-ds/15_IDE/'
# file_name = 'main.py'
# print(count)
#
# for dirs in os.listdir(my_dir):
#     print()
#     print(dirs)
#     for file in os.listdir(os.path.join(my_dir, dirs)):
#         print('   ', file)
#         if file == file_name:
#             print('   ', os.path.join(my_dir, dirs, file), end=' - ')
#             print('Размер файла -', os.path.getsize(os.path.join(my_dir, dirs, file)), 'байт!')
#             my_read = open(os.path.join(my_dir, dirs, file), 'r', encoding= 'UTF-8')
#             my = my_read.read()
#             print(my)
#             print()


