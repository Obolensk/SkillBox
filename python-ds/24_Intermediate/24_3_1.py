
text = input('Введите текст: ')

with open('24_3_1.txt', 'w', encoding='utf-8') as file:
    file.write(text)