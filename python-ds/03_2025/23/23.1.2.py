import os

my_dir = 'C:/Users/e.menshaev/PycharmProjects/SkillBox/python-ds'
new_dir = os.path.dirname(my_dir)
new_dir_1 = os.path.dirname(new_dir)

print(my_dir)
print(new_dir)
print(new_dir_1)
print()

print(os.listdir(new_dir_1))
import os

folder = 'C:/Users/ASUS/Desktop/SkillBox'
my_dir = os.listdir(folder)
print('\nСодержимое каталога', os.path.abspath(folder))
print()

# print(my_dir)

for i in my_dir:
    print(os.path.abspath(i))