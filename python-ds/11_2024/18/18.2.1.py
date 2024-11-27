left = 5
right = 10
new_list = []

for i in range(left, right + 1):
    new_list.append(i ** 2)

print(new_list)

new_exp = [i ** 3 for i in range(left, right + 1)]
print(new_exp)