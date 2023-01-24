# TODO здесь писать код

new_file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/02_zen_of_python/zen.txt', 'r',
                encoding='UTF-8')

zen = new_file.read()
zen_list = []

for i in zen.split('\n'):
    zen_list.append(i)

for i in range(len(zen_list)-1, -1, -1):
    print(zen_list[i])
