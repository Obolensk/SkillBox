import os

print('Содержимое каталога {}'.format(os.getcwd()))

for i in os.listdir('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/'):
    print(os.path.abspath(i))
