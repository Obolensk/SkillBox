# TODO здесь писать код

def sim(obj):
  rnd = int(input('Введите случайный элемент: '))

  if rnd not in obj:
    print()

  count = 0
  new_list = []

  for i in obj:
    if i == rnd:
      count += 1
    if count == 1:
      new_list.append(i)
    if count == 2:
      new_list.append(i)
      break

  return tuple(new_list)


my_tup = ('h', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 8, 12, 13, 14)

print(sim(my_tup))

