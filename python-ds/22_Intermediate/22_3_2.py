

# ТАК И НЕ РЕШИЛ!!!




my_data = input('Введите данные: ')
print(round(float(my_data)))
print(int(float(my_data)))

print(type(my_data))

if type(my_data) == str:
  tpd = 'str (строка)'

elif float(my_data):
  if float(my_data) % 1 == 0:
    tpd = 'int (Целое число)'
  else:
    tpd = 'float (Число с плавающей точкой)'
else:
  tpd = 'str (строка)'

print('Тип данных: {0}'.format(tpd))
