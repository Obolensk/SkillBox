a = int(input('a = '))
b = int(input('b = '))
print()

my_list = [i for i in range(a, b + 1) if i % 2 == 0]

print(my_list)