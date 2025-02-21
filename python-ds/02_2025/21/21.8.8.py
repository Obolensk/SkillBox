phone_book = {
    'Tom': 111111,
    'Ann': 222222,
    'Tim': 333333,
    'Pit': 444444,
    'John': 555555,
    'Steve': 777777
}

print(phone_book)

while True:
    ans = int(input('Введите действие, 1 - добавить, 2- найти: '))

    if ans == 1:
        name = input('Введите имя: ')
        num = input('Введите номер телефона: ')
        phone_book[name] = num
    elif ans == 2:
        search_name = input('Введите имя: ')
        print('Номер телефона контакта по имени {} - {}'.format(search_name, phone_book[search_name]))
    else:
        break


print(phone_book)



