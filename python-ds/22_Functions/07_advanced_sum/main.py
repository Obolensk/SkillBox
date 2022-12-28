# TODO здесь писать код


def sum(*args):
  if not any(type(arg) == list for arg in args):
    result = 0
    for arg in args:
      result += arg
      # print('arg = ', arg)
      # print('result = ', result)
      # print()
    return result
  lst = []
  for arg in args:
    if type(arg) != list:
      lst.append(arg)
    else:
      lst.extend(arg)
  return sum(*lst)

print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))
