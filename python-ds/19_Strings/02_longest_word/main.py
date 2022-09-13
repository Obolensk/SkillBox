# TODO здесь писать код

my_text = input('Введите строку: ').split()

letter_count = 0
letter_count_list = []
for word in my_text:
    for letter in word:
        letter_count += 1
    letter_count_list.append(letter_count)
    letter_count = 0

print('Самое длинное слово: {0}'.format(my_text[letter_count_list.index(max(letter_count_list))]))
print('Длина этого слова: {0}'.format(max(letter_count_list)))