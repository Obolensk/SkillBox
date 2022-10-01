# my_str = input('Введите строку: ')
my_str = 'Я! Есть. Грут?! Я, Грут и Есть.'.split()
# print(my_str)
# new_str = []

# k = 0
# for word in my_str:
#   # print(word)
#   for sym in word:
#     if sym.isalpha():
#       continue
#     else:
#       new_str.append(sym)

# # print(new_str)

# print()
# print('Количество знаков пунктуации:', len(new_str))

my_set = set(my_str)
print(my_set)

sym_count = 0
for word in my_set:
    print(word)
    for sym in word:
        # print(sym)
        if not sym.isalpha():
            sym_count += 1
print(sym_count)
