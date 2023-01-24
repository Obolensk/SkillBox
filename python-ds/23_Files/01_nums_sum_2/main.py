# TODO здесь писать код

import os

new_file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/01_nums_sum_2/numbers.txt', 'r',
                encoding='UTF-8')

# print(new_file)

my_nums = new_file.read()
my_sum = 0
for i in my_nums.split():
    my_sum += int(i)

print(my_sum)



result = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/01_nums_sum_2/answer.txt', 'w',
                encoding='UTF-8')
result.write(str(my_sum))


#
# for i in os.listdir('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/15_IDE/07_years'):
#     script = open(os.path.join('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/15_IDE/07_years', i), 'r',
#                   encoding='UTF-8')
#     my_script = script.read()
#     print(i)
#     print(my_script)
#     new_file.write(my_script)
#     new_file.write('\n ')
#     new_file.write('\n****************************************')
#     new_file.write('\n ')