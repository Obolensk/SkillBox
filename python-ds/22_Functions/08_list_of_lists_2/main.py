nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

# TODO здесь писать код



def myl(arg):
  lst = []
  for mem in arg:
    # print()
    # print(mem)
    # print(type(mem))
    if type(mem) == list:
      lst.extend(myl(mem))
      # print('lst = ', lst)
      # print()
    else:
      lst.append(mem)
      # print('lst = ', lst)
      # print()
  return lst

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(myl(nice_list))


