data = {
  (5000, 123456): ('Иванов', 'Василий'),
  (6000, 111111): ('Иванов', 'Петр'),
  (7000, 222222): ('Медведев', 'Алексей'),
  (8000, 333333): ('Алексеев', 'Георгий'),
  (9000, 444444): ('Георгиева', 'Мария')
}

print(data)

num = int(input('Введите серию и номер: '))
ser = int(input('Введите номер: '))

for keys in data:
  # print(111111 in keys)
  # print(keys)
  # print(data[keys])
  if num in keys and ser in keys:
    print('Серия паспорта {0} и номер паспорта {1} соответствует товарищу по имени {3} и по фамилии {2}'.format(ser, num, data[keys][0], data[keys][1]))
