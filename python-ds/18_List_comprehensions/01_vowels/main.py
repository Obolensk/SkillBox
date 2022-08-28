# TODO здесь писать код

my_text = input('Введите текст: ')
vowels = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
list = [sym for sym in my_text if sym in vowels]
print('Список гласных букв:', list)
print('Длина списка:', len(list))