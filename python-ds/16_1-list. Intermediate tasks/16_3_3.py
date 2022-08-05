i = 1
word_list = []

while i <= 3:
    print('Введите', i, end=' ')
    i += 1
    word = input('слово: ')
    word_list.append(word)
# print(word_list)

print()
text = []
while True:
    text_word = input('Слово из текста: ')
    text.append(text_word)
    if text_word == 'end':
        break
# print(text)

print()
print('Подсчёт слов в тексте')

word_count = 0

for i in range(3):
    for single_word in text:
        if single_word == word_list[i]:
            word_count += 1
    print(word_list[i], ':', word_count)
    word_count = 0



