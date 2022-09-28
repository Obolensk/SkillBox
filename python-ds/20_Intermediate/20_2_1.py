
small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)

item = input('Название товара: ')
if big_storage.get(item) == None:
    print('Товара {} нет на складе'.format(item))
else:
    print('Количество товара {0} на складе равно {1} штук'.format(item, big_storage.get(item)))