# TODO здесь писать код

phone_book = {
  ('Иванов', 'Иван'): 654789,
  ('Петров', 'Петр'): 123456
             }

while True:
  ask = input('Введите действие добавить или найти: ')

  if ask == 'добавить':
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    if (surname, name) in phone_book:
      print('Такой абонент уже есть!')
      continue
    else:
      num = input('Введите номер телефона: ')
      phone_book[(surname, name)] = num
      print(phone_book)
      
  elif ask == 'найти':
      search = input('Введите фамилию: ')
      for name in phone_book:
        if search.lower() in name[0].lower():
          print(name[0], name[1], phone_book[name])
    
  else:
    print('Введите слово "найти" или "добавить"')
    
