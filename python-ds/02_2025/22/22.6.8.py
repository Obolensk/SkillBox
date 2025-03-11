
nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]



lst = []

def unzip(seq):
    for elem in seq:
        if isinstance(elem, list):
            unzip(elem)
        else:
            lst.append(elem)
    return lst

print(unzip(nice_list))



