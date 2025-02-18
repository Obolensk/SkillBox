phone_book = {
    ('Иванов', 'Иван'): 456789,
    ('Сергеев', 'Сергей'): 321654,
    ('Петров', 'Петр'): 369852,
    ('Алексеев', 'Алексей'): 741258
}

print(phone_book)

while True:
    new = input('Введите через пробел Фамилию Имя и телефон нового контакта: ')
    if new == 'end':
        break
    elif (new.split()[0], new.split()[1]) in phone_book:
        print('Такой абонент уже есть!')
        continue
    else:
        phone_book[(new.split()[0]), new.split()[1]] = new.split()[2]
        print(phone_book)


print(phone_book)
