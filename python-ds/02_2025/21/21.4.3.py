
my_dict = {
    0: 0,
    1: 100,
    2: 144,
    3: 19
}

print(my_dict)

# print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19} if {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] % 2 == 0])

my_list = []
for key, value in my_dict.items():
    if key % 2 == 0:
        my_list.append(value)
print(my_list)

ml = [v for k, v in my_dict.items() if k % 2 == 0]
print(ml)