# TODO здесь писать код

abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
abc_list = [i for i in abc]
# print(abc_list)

text = input('Введите сообщение: ').lower()
text_list = [i for i in text]
# print(text_list)
shift = int(input('Введите сдвиг: '))

new_text = [(abc_list[(abc_list.index(text_list[i]) + shift) % 33] if text_list[i] != ' ' else ' ')
            for i in range(len(text_list))]

print(''.join(new_text))