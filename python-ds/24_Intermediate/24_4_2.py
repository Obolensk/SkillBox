
with open('words.txt', 'r', encoding='utf-8') as file:
    for name in file.read().split():
        print(name)
        count = 0
        for lit in name:
            count += 1
        print('Количество букв в слове равно - {}'.format(count))
        if count <= 3:
            print('ОШИБКА. В имени меньше трех букв!!!')
            break
        else:
            continue