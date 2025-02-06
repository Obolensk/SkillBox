
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

small_storage.update(big_storage)

print(small_storage)

item = input('Введите интересующий товар: ')
if item in small_storage:
    print('Товар {} на складе имеется в количестве {} штук'.format(item, small_storage.get(item)))
else:
    print('Товара {} на складе нет'.format(item))