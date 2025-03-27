import os

# pt = '..//'
# print('Содержимое папки:', os.path.abspath(pt))
#
# for i in os.listdir(pt):
#     print(i)


path1 = 'C:/Users/ASUS/Desktop/SkillBox/python-ds/03_2025/23'
path2 = 'C:/Users/ASUS/Desktop/SkillBox/python-ds/03_2025/23/23.2.1.py'
path = 'https://go.skillbox.ru/profession/profession-data-scientist/python-for-data-science/'
print(path)
print(os.path.isdir(path))
print(os.path.isfile(path1))
print(os.path.getsize(path1))
print(os.path.islink(path))

if os.path.isdir(path):
    print('Это директория!')
elif os.path.isfile(path):
    print('Это файл, он весит', os.path.getsize(path), 'kB')
else:
    print('Указанного пути не существует!')