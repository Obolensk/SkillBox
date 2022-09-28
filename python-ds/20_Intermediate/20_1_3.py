
name = ''
phone_book = {}

while name != 'q':
    # phone_book[input('Введите имя: ')] = input('Введите номер телефона: ')
    name = input('Введите имя: ')
    if name in phone_book:
        print('Ошибка! Имя {0} в телефонной книге уже есть'.format(name))
    else:
        phone_book[name] = input('Введите номер телефона: ')
        print(phone_book)


