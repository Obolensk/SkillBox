
path = input('Путь к файлу: ')
disc = input('На каком диске должен лежать файл: ')
ext = input('Требуемое расширение файла: ')

if not path.startswith(disc):
    print('Ошибка!')
elif not path.endswith(ext):
    print('Ошибка!')
else:
    print('Путь корректен!')
