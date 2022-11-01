# TODO здесь писать код


n = int(input('Сколько записей вносится в протокол? '))
my_dict = {}

for i in range(n):
  print(i+1, end=' ')
  rec = input('запись: ').split()
  my_dict[i] = rec

fst = '0'
sec = '0'
thr = '0'
name_1 = ''
name_2 = ''
name_3 = ''

for i in my_dict:
  if int(my_dict[i][0]) > int(fst):
    if my_dict[i][1] != name_1:
      thr = sec
      sec = fst
      fst = my_dict[i][0]
      name_3 = name_2
      name_2 = name_1
      name_1 = my_dict[i][1]
    else:
      fst = my_dict[i][0]
      name_1 = my_dict[i][1]
  elif int(my_dict[i][0]) > int(sec):
    if my_dict[i][1] != name_1:
      thr = sec
      sec = my_dict[i][0]
      name_3 = name_2
      name_2 = my_dict[i][1]
    else:
      sec = my_dict[i][0]
      name_2 = my_dict[i][1]
  elif int(my_dict[i][0]) > int(thr):
    thr = my_dict[i][0]
    name_3 = my_dict[i][1]
    
print()
print('1 место. {0} ({1})'.format(name_1, fst))
print('2 место. {0} ({1})'.format(name_2, sec))
print('3 место. {0} ({1})'.format(name_3, thr))


