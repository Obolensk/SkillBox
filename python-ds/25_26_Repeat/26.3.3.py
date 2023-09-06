
list = []
with open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/25_26_Repeat/nums.txt', 'r', encoding='utf-8') \
        as file:
    for i in file.read().split():
        print(i)
        list.append(i)

print(list)

class DivisionError(Exception):
    pass


# for i in range(0, len(list), 2):
#     print(i)
#     if int(list[i]) / int(list[i+1]) > 1:
#         print(int(list[i]), '/', int(list[i+1]), '=', int(list[i]) / int(list[i+1]))
#     else:
#         DivisionError('Exception')
#         # print('ERROR!!!!')

for i in range(0, len(list), 2):
    print(i)
    try:
        int(list[i]) / int(list[i+1])
        print(int(list[i]), '/', int(list[i + 1]), '=', int(list[i]) / int(list[i + 1]))
    except DivisionError:
        print('нельзя делить большее на меньшее')
    #     print(int(list[i]), '/', int(list[i+1]), '=', int(list[i]) / int(list[i+1]))
    # else:
    #     DivisionError('Exception')
    #     # print('ERROR!!!!')