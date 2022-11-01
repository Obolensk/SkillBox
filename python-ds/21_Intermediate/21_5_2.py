phone_book = {('Иванов', 'Иван'): 654789}

while True:
  surname = input('Введите фамилию: ')
  name = input('Введите имя: ')
  if (surname, name) in phone_book:
    print('Такой абонент уже есть!')
    continue
  else:
    num = input('Введите номер телефона: ')
    phone_book[(surname, name)] = num
    print(phone_book)


