# TODO здесь писать код
all_syms = 0
str_count = 0
with open('people.txt', 'r', encoding='utf-8') as file:
    for name in file.read().split():
        # print(name)
        count = 0
        str_count += 1
        for lit in name:
            count += 1
        # print('Количество букв в слове равно - {}'.format(count))
        all_syms += count
        if count <= 3:
            print('ОШИБКА. В имени {} в строке {} меньше трех букв!!!'.format(name, str_count))
        else:
            continue

print('Общее количество символов:', all_syms)




