
def sym_count(msg):
    letter_count = 0
    for letter in msg:
        if letter == '!' or letter == '?':
            letter_count += 1
    return(letter_count)

fir_msg = input('Первое сообщение: ')
sec_msg = input('Второе сообщение: ')

if (sym_count(fir_msg)) > (sym_count(sec_msg)):
    print(fir_msg, sec_msg)
if (sym_count(fir_msg)) < (sym_count(sec_msg)):
    print(sec_msg, fir_msg)
if (sym_count(fir_msg)) == (sym_count(sec_msg)):
    print('Ой')

