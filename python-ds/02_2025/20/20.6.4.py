
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
cost = 0
quantity = 0
for item in goods:
    for code in store:
        if goods[item] == code:
            for i in range(len(store[code])):
                quantity += store[code][i]['quantity']
                cost += store[code][i]['quantity'] * store[code][i]['price']
            print('{} - {} шт. Стоимость {} руб.'.format(item, quantity, cost))
            quantity = 0
            cost = 0

# Каждая запись второго словаря отображает, сколько и по какой цене закупалось товаров (цена указана за 1 шт.).
# Напишите программу, которая рассчитывает, на какую сумму лежит каждого товара на складе, и выводит эту информацию на экран.
# Результат работы программы.
# Лампа - 27 шт, стоимость 1134 руб
# Стол - 54 шт, стоимость 27860 руб
# Диван - 3 шт, стоимость 3550 руб
# Стул - 105 шт, стоимость 10311 руб


