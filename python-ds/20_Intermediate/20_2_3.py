# text = input('Введите текст:')
text = 'Здесь что-то написано'

print(text)
print()

sym_dict = dict()
for sym in text:
    if sym in sym_dict:
        sym_dict[sym] += 1
    else:
        sym_dict[sym] = 1

print(sym_dict)
for sym in sorted(sym_dict):
    print(sym, ' - ', sym_dict[sym])

print()
print('Максимальная частота:', max(sym_dict.values()))