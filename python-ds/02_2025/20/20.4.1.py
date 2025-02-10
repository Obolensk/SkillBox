my_set = set(['.', ',', ';', ':', '!', '?'])

# print(my_set)
#
# print('.' in my_set)

my_text = 'Я! Есть. Грут?! Я, Грут и Есть.'
sym_count = 0


for sym in my_text:
    if sym in my_set:
        sym_count += 1

print('Количество знаков пунктуации: ', sym_count)