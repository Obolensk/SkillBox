wrong_sym = ['@', '№', '$', '%', '^', '&', '*', '()']
right_ext = ['.txt', '.docx']


name_1 = '@example.txt'
name_2 = 'example.ttxt'
name_3 = 'example.txt'


def check_name(file_name):
    print('\n Файл - ', file_name)
    for sym in wrong_sym:
        if file_name.startswith(sym):
            print('Ошибка: название начинается на один из специальных символов.')
            break
        else:
            for ext in right_ext:
                if file_name.endswith(ext):
                    print('Файл назван верно')
                    break
                else:
                    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
                    break
            break


check_name(name_1)
check_name(name_2)
check_name(name_3)
