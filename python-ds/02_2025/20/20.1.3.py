

phone_book = dict()

while True:
    name = input('Введите имя: ')
    if name in phone_book:
        print('Ошибка: такое имя уже существует.')
        continue
    elif name == 'end':
        break
    number = input('Введите номер телефона: ')
    phone_book[name] = number
    print(phone_book)