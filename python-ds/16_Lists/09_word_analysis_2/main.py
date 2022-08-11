# TODO здесь писать код

word = input('Введите слово: ')
new_word = []
word_reverse = []

for i in word:
    new_word.append(i)
# print(new_word)

for i in range(len(word)):
    word_reverse.append(new_word[-1-i])
# print(word_reverse)

if new_word == word_reverse:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
