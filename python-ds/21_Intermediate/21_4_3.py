# print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19} if {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] % 2 == 0])

my_dict = {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}
new_list = []
for key, value in my_dict.items():
  if key % 2 == 0:
    new_list.append(value)

print(new_list)


# [0, 100, 144, 20]

