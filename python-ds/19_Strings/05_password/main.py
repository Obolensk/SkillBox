# TODO здесь писать код

while True:
    password = input('Придумайте пароль: ')
    letter_count = 0
    up_case = 0
    nums = 0

    for letter in password:
        if letter.isupper():
            up_case += 1
        if letter.isdigit():
            nums += 1
        letter_count += 1
    if letter_count < 8 or up_case < 1 or nums < 3:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
