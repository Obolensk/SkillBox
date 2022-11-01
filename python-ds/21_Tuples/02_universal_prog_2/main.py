# TODO здесь писать код


def is_prime(a):
  if a <= 1:
    return False
  else:
    if a != 2 and a % 2 == 0 or a != 3 and a % 3 == 0:
      return False
    else:
      return True

def sim(obj):
  lst = []
  for i in range(len(obj)):
    if is_prime(i):
      lst.append(obj[i])
    else:
      continue
  return lst

my_list = ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
my_str = 'О Дивный Новый мир!'
my_dict = {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}
my_tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

print(sim(my_dict))
