# TODO здесь писать код

import zipfile

# vim = zipfile.ZipFile('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/09_war_and_peace/voyna-i-mir.zip')
#
# for file in vim.namelist():
#     vim.extract(file, 'C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/09_war_and_peace')
# vim.close()

new_vim = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/09_war_and_peace/voyna-i-mir_short.txt', 'r',
               encoding='UTF-8')

text = new_vim.read()

l_count = 0

zen_list = ''
my_list = ''
my_dict = {}

for i in text:
    if i.isalpha():
        zen_list += i

# print(zen_list)

for a in zen_list:
    for b in zen_list:
        if a == b:
            l_count += 1
    if a not in my_list:
        my_list += a
        my_dict[a] = l_count
    l_count = 0

# print(my_list)

# print(sorted(my_dict.items(), key=lambda x: x[1]))
# print()

for i in sorted(my_dict.items(), key=lambda x: x[1]):
    print(i)

