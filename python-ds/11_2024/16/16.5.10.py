

# 16.5.10

# word = 'мадам'
word = input('Введите слово: ')
word_list = list(word)
word_reverse = []
l = list(word)
# print(l)
# print(l.reverse())
# print(len(word))
for i in range(1, len(word) + 1):
    word_reverse.append(word[len(word) - i])

# print(word_list)
# print(word_reverse)

if word_list == word_reverse:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

