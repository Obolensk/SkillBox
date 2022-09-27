# TODO здесь писать код

msg = input('Сообщение: ')

msg_1 = ''
new_msg = ''

for sym in msg:
    if sym.isalpha():
        msg_1 += sym
    else:
        msg_1 = msg_1[::-1]
        new_msg += msg_1
        new_msg += sym
        msg_1 = ''

for new_word in new_msg:
    print(''.join(new_word), end='')
