

tup_1 = (6, 8, 5, 1, 3, 2, 0, 9, 4, 7)
tup_2 = (6, 8, 5, 1, 3, '2', 0, 9, 4, 7)
new_tup = []

# print(tuple(sorted(list(tup))))
# print(sorted(list(tup_1)))

def tup_func(tup, a = 0):
    lst = []
    for num in tup:
        # print(num, type(num))
        if type(num) != int:
            print('В кортеже не все элементы являются целыми числами')
            a = 1
            break
        else:
            lst.append(num)
            a = 0
    if a == 0:
        return sorted(lst)
    else:
        return tup

print('\n\ttup 1')
print(tup_func(tup_1))
print('\n\ttup 2')
print(tup_func(tup_2))



