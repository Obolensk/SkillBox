
let = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
text = input('Введите текст: ')

new_list = []

for i in text:
    if i in let:
        new_list.append(i)

print('Список гласных букв:', new_list)
print('Длина списка:', len(new_list))
