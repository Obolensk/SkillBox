# Путь к файлу: C:/user/docs/folder/new_file.txt
# На каком диске должен лежать файл: C
# Требуемое расширение файла: .txt
# Путь корректен!

path = 'C:/user/docs/folder/new_file.txt'
disc = 'C'
ext = 'txt'

if path.startswith(disc) and path.endswith(ext):
    print('Путь корректен!')
else:
    print('Путь НЕкорректен!')