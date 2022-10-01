my_str = 'ab1n32kz2'
my_set = set()
for sym in my_str:
  if not sym.isalpha():
    my_set.add(sym)

print('Различные цифры строки:', ''.join(sorted(my_set)))

