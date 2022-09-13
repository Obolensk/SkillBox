
my_words = input('Введите 3 слова через запятую: ').split(', ')
print(my_words)

text = input('Введите текст: ')

word_count = 0
for word in my_words:
    if word in text:
        word_count += 1

print(word_count)
