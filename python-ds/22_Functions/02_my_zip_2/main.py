# TODO здесь писать код

def my_zip(data_1, data_2, *args):
  for i in range(len(data_1)):
    for my_args in args:
      tpl = (data_1[i], data_2[i], my_args[i])
      print(tpl)

my_str = 'abcd'
my_tpl = (10, 20, 30, 40)

my_zip(my_str, my_tpl, [1, 2, 3, 4, 5, 6])
