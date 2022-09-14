# TODO здесь писать код

# msg = input('Сообщение: ').split()
msg = 'Это задание очень! простое.'.split()
# syms = ['.', ',', '!', '?', ':', ';']

# print(msg)
# print(msg[1])

list = []
for word in msg:
    for letter in word:
        list.append(letter)
    print(''.join(list[::-1]), end=' ')
    list = []

#

