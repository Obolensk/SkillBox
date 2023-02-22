
with open('words.txt', 'r', encoding='utf-8') as file:
    pal_count = 0
    for name in file.read().split():
        print(name)
        if name == ''.join(reversed(name)):
            pal_count += 1
        for sym in name:
            if sym.isdigit():
                with open('errors.log', 'a', encoding='utf-8') as logs:
                    logs.write('В слове {} имеется число {} \n'.format(name, sym))
            # print(sym)
            # print(sym.isdigit())
            # print()
    print('Количество палиндромов в файле равно {}'.format(pal_count))


