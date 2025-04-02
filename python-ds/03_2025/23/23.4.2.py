import os

folder = os.path.abspath('C:/Users/e.menshaev/PycharmProjects/SkillBox/python-ds/02_2025/22')
print(folder)
print(os.listdir(folder))

for script in os.listdir(folder):
    print(script)
    path = os.path.join(folder, script)
    file = open(path, 'r', encoding='utf-8')
    scr = file.read()
    rec = open('scripts.txt', 'a', encoding='utf-8')
    rec.write(scr)
    rec.write('\n\n\n              **************************\n\n\n')
    file.close()

rec.close()




