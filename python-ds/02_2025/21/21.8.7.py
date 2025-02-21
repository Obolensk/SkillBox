

tup_1 = (6, 8, 5, 1, 3, 2, 0, 9, 4, 7)
tup_2 = (6, 8, 5, 1, 3, '2', 0, 9, 4, 7)
new_tup = []
# print(tuple(sorted(list(tup))))
# print(sorted(list(tup_1)))

def tup_func(tup):
    lst = []
    for num in tup:
        # print(num, type(num))
        if type(num) != int:
            print('В кортеже не все элементы являются целыми числами')
            return tup
            break
        else:
            lst.append(num)
    return sorted(lst)


print(tup_func(tup_1))
print(tup_func(tup_2))



