# TODO здесь писать код

abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
abc_list = [i for i in abc]
# print(abc_list)

text = input('Введите сообщение: ')
text_list = [i for i in text]
# print(text_list)
shift = int(input('Введите сдвиг: '))

new_text = []
for i in range(len(text_list)):
    if text_list[i] == ' ':
        new_text.append(' ')
    elif abc_list.index(text_list[i]) + shift >= len(abc_list):
        new_text.append(abc_list[len(abc_list) - abc_list.index(text_list[i]) - shift])
    else:
        new_text.append(abc_list[abc_list.index(text_list[i]) + shift])

print(''.join(new_text))