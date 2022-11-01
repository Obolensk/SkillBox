# TODO здесь писать код

my_tup = (5, 6, 2)
# lst = tuple(sorted(list(tup)))
# print(tup)
# print(lst)


def tup_sort(tup):
  for sym in tup:
    if sym == int(sym):
      k = 1
    else:
      k = 2
  if k == 1:
    return tuple(sorted(list(tup)))
  else:
    return tup
  
print(tup_sort(my_tup))

