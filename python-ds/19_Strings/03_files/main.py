# TODO здесь писать код

name = input('Название файла: ')

sym_list = ['@', '№', '$', '%', '^', '&', '*', '()']
ext_list = ['.txt', '.docx']

for sym in sym_list:
    if name.startswith(sym):
        print('Ошибка: название начинается на один из специальных символов.')
        break
    else:
        if name.endswith('.txt') or name.endswith('.docx'):
            print('Файл назван верно.')
            break
        else:
            print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
            break

