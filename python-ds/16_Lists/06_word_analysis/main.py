# TODO здесь писать код

word = input('Введите слово: ')
new_list = []

for sym in word:
    new_list.append(sym)
# print('new_list - ', new_list)
# print('word - ', word)
uniq = 0
count = 0
for letter in word:
    for i in range(len(new_list)):
        if new_list[i] == letter:
            count += 1
    # print(letter, 'встречается в слове', count, 'раз')
    if count == 1:
        uniq += 1
    count = 0
print('Количество уникальных букв: ', uniq)
