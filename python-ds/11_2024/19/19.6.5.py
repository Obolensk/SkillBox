
pass_1 = 'qwerty'
pass_2 = 'qwerty12'
pass_3 = 'qwerty123'
pass_4 = 'qWErty123'

# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qWErty123
# Это надёжный пароль!

def check_pass(password):
    print('\nПароль: ', password)
    sym = 0
    up = 0
    num = 0
    for i in password:
        sym += 1
        if i.isupper():
            up += 1
        if i.isdigit():
            num += 1
    print('Количество символов - {}, Количество заглавных букв - {}, Количество цифр - {}'.format(sym, up, num))

    if sym < 8 or up < 1 or num < 3:
        print('Пароль ненадёжный. Попробуйте ещё раз')
    else:
        print('Это надёжный пароль!')




check_pass(pass_1)
check_pass(pass_2)
check_pass(pass_3)
check_pass(pass_4)