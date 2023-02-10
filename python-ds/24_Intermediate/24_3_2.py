

try:
    new_file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/24_Intermediate/zen.txt', 'r',
                    encoding='UTF-8')

    zen = new_file.read()
    zen_list = []

    for i in zen.split('\n'):
        zen_list.append(i)

    for i in range(len(zen_list)-1, -1, -1):
        print(zen_list[i])
except FileNotFoundError:
    print('Мы попытались открыть и прочитать несуществующий файл!!!')
else:
    print('Все сработало хорошо!')
finally:
    print('Закончили упражнение!!!')