
with open('people.txt', 'r', encoding='utf-8') as file:
    for name in file.read().split():
        # print()
        sym_count = 0
        for lit in name:
            # print(lit)
            sym_count += 1
        if sym_count < 3:
            print('Error!!! В имени {} меньше трех букв. Программа завершена'.format(name))
            break