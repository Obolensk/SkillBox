# TODO здесь писать код


order_nums = int(input('Введите кол-во заказов: '))

order_dict = {}

for i in range(order_nums):
  print(i + 1, 'заказ: ', end = '')
  pair = input('').split()
  if pair[0] not in order_dict:
    order_dict[pair[0]] = {pair[1]: int(pair[2])}
  else:
    if pair[1] not in order_dict[pair[0]]:
      order_dict[pair[0]][pair[1]] = int(pair[2])
    else:
      order_dict[pair[0]][pair[1]] += int(pair[2])

print()

for name in sorted(order_dict):
  print(name, ':')
  for pizza in order_dict[name]:
    print('\t', pizza, ':', order_dict[name][pizza])

