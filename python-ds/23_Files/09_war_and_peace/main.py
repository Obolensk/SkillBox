# TODO здесь писать код

import zipfile

vim = zipfile.ZipFile('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/09_war_and_peace/voyna-i-mir.zip')
#
for file in vim.namelist():
    vim.extract(file, 'C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/09_war_and_peace')
vim.close()

vim = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/09_war_and_peace/voyna-i-mir.txt', 'r',
               encoding='UTF-8')

text = vim.read()

zen_list = ''
my_list = ''
my_dict = {}

for i in text:
    if str(i).isalpha():
        zen_list += i

for a in zen_list:
    if a not in my_list:
        my_list += a

for i in my_list:
    my_dict[i] = zen_list.count(i)

for i in sorted(my_dict.items(), key=lambda x: x[1]):
    print(i)