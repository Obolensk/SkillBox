import os

folder = 'C:/Users/ASUS/Desktop/SkillBox'
my_dir = os.listdir(folder)
print('\nСодержимое каталога', os.path.abspath(folder))
print()

# print(my_dir)

for i in my_dir:
    print(os.path.abspath(i))