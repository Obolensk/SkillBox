goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код

q = 0
cost = 0
print()
for good in goods:
  print(good, '- ', end = '')
  for i in range(len(store[goods[good]])):
    q += store[goods[good]][i]['quantity']
    cost += store[goods[good]][i]['quantity'] * store[goods[good]][i]['price']
  print(q, 'шт.', end = ' ')
  print('cтоимость', cost, 'руб')
  print()
  q = 0
  cost = 0
