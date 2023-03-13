# TODO здесь писать код

user = input('Введите имя пользователя: ')
while True:
    act = input('Введите действие (1 - Посмотреть текущий текст чата, 2 - Отправить сообщение): ')
    if act == '1':
        with open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/24_Exceptions/06_chat/chat.txt', 'r', encoding='utf-8') \
                as file:
            print(file.read())
    elif act == '2':
        msg = input('Введите сообщение: ')
        with open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/24_Exceptions/06_chat/chat.txt', 'a', encoding='utf-8') \
                as file:
            file.write('ПОЛЬЗОВАТЕЛЬ: {}'.format(user))
            file.write('\n')
            file.write('СООБЩЕНИЕ: {}'.format(msg))
            file.write('\n')





