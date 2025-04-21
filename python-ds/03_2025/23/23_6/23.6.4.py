import os

my_path = 'C:/Users/e.menshaev/PycharmProjects/SkillBox/python-ds/03_2025/23/23_6'
new_path = 'C:/Users/e.menshaev/PycharmProjects/SkillBox/python-ds/03_2025/23/23.1.1.py'

print()
ab = os.path.abspath(my_path)
print('Абсолютный путь:', ab)
print('Размер каталога (в Кб):', os.path.getsize(ab))
print(os.listdir(ab))
dir_count = 0
files = 0

for i in os.listdir(ab):
    if os.path.isdir(i):
        dir_count += 1
    else:
        files += 1

print('\nКоличество подкаталогов:', dir_count)
print('Количество файлов:', files)


