

def is_poly(string):
    my_dict = dict()
    odd_count = 0
    for sym in string:
        my_dict[sym] = my_dict.get(sym, 0) + 1
    for values in my_dict.values():
        if values % 2 != 0:
            odd_count += 1
    return odd_count <= 1


my_string = input('Введите строку: ')

if is_poly(my_string):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')