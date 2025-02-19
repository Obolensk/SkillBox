

tup = (1, 2, 'три', 'IV', 3, ['f', 0], 2, 't')

def func(col, sym):
    lst = []
    count = 0
    for item in col:
        if item == sym:
            count += 1
        # print('item = ', item)
        # print('count = ', count)
        if count == 1 or item == sym:
            lst.append(item)
    return tuple(lst)

print(func(tup, 2))
print(func(tup, 3))



