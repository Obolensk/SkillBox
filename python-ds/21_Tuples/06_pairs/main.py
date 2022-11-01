# TODO здесь писать код

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0
lst_1 = []
lst_2 = []
for sym in my_list:
  lst_1.append(sym)
  count += 1
  if count == 2:
    lst_2.append(tuple(lst_1))
    count = 0
    lst_1 = []

print(lst_2)
