
try:
    abc = 'abc de'
    dct = {}
    k = 0

    with open('ages.txt', 'r', encoding='utf-8') as ages:
        for age in ages:
            dct[abc[k]] = age
            k += 1

    with open('result.txt', 'x', encoding='utf-8') as res:
        for i in dct:
            res.write(i)
            res.write(' - ')
            res.write(dct[i])
except FileExistsError:
    print('Файл-то уже давно есть!!!!')
except PermissionError:
    print('Данные можно записывать только в файлы!!! Не в директории!!!')
except TypeError:
    print('Ну тут 2 варианта: любо тип даных либо некорректное значение???')


