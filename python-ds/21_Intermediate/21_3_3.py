my_str = 'О Дивный Новый мир!'

my_list = []
ind = 0
for sym in my_str:
  if ind % 2 == 0:
    my_list.append(sym)
  ind += 1

print(my_list)
