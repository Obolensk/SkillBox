
def get_question(question,
                 message='Неверный ввод. Пожалуйста, введите "да" или "нет".',
                 retries=3):
    ask = input(question)
    if ask == 'да':
        retries -= 1
        print('Осталось попыток:', retries)
    elif ask == 'нет':
        retries -= 1
        print('Осталось попыток:', retries)
    else:
        print(message)
        retries -= 1
        print('Осталось попыток:', retries)


get_question('Вы действительно хотите выйти? ')
get_question('Удалить файл? ', 'НЕПРАВИЛЬНО!!!!')
get_question('Записать файл?  ', retries=10)


