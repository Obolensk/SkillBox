# TODO здесь писать код

new_file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/08_frequency_analysis/text.txt', 'r',
                encoding='UTF-8')
let = 0
l_count = 0

zen = new_file.read()
zen_list = []
my_list = ''
my_dict = {}

print('zen = ', zen)

for i in zen:
    if i.isalpha():
        zen_list.append(i)
print('zen_list = ', zen_list)

res = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/08_frequency_analysis/analysis.txt', 'a')

for a in range(len(zen_list)):
    for b in range(len(zen_list)):
        if zen_list[a].lower() == zen_list[b].lower():
            l_count += 1
    if zen_list[a].lower() not in my_list:
        my_list += zen_list[a].lower()
        res.write('{} {} \n'.format(zen_list[a].lower(), round(l_count/len(zen_list), 3)))
    l_count = 0



