
import random

# x_list = ['a', 'b', 'c']
for i in['a', 'b', 'c']:
    print(i)


print()

cell_list = []
for x_coord in ['a', 'b', 'c']:
    for y_coord in range(3):
        cell_list.append(x_coord + str(y_coord+1))

print(cell_list)

print()
# list = ['a', 'b', 'c', 'd']
print(['a', 'b', 'c', 'd'][random.randint(0, 3)])
