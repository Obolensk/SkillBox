# TODO здесь писать код

my_dict = {
  ' ': 2,
  '-': 1,
  'З': 1,
  'а': 2,
  'д': 1,
  'е': 1,
  'и': 1,
  'н': 2,
  'о': 3,
  'п': 1,
  'с': 2,
  'т': 2,
  'ч': 1,
  'ь': 1
}

vals = []
for val in my_dict.values():
  if val not in vals:
    vals.append(val)

res = dict()
my_list = []

for k in vals:
  res[k] = my_list
  for v in my_dict.keys():
    if my_dict[v] == k:
      my_list.append(v)
  my_list = []

print(res)


