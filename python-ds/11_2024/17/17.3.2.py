

def sym_count(text, first_sym, second_sym):
    count = 0
    for sym in text:
        if sym == first_sym or sym == second_sym:
            count += 1
    return count

# print(sym_count('Привет, Андрей', 'е', 'й'))

first_mes = input('Первое сообщение: ')
second_mes = input('Второе сообщение: ')

if sym_count(first_mes, '!', '?') > sym_count(second_mes, '!', '?'):
    print(first_mes, second_mes)
elif sym_count(first_mes, '!', '?') < sym_count(second_mes, '!', '?'):
    print(second_mes, first_mes)
else:
    print('Ой!')


