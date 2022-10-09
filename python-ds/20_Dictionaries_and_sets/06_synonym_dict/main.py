# TODO здесь писать код


word_nums = int(input('Введите количество пар слов: '))

word_dict = dict()
for i in range(word_nums):
  print(i + 1, 'пара: ', end = '')
  pair = input('').split(' - ')
  word_dict[pair[0].lower()] = pair[1].lower()

my_keys = list(word_dict.keys())
my_values = list(word_dict.values())

while True:
  new_word = input('Введите слово: ').lower()
  if new_word in word_dict.keys():
    print('Синоним:', word_dict[new_word])
    break
  elif new_word in word_dict.values():
    print('Синоним:', my_keys[my_values.index(new_word)])
    break
  else:
    print('Такого слова в словаре нет.')
