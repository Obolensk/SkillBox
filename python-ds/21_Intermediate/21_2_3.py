first_list = []
second_list = []
third_list = []

for i in range(6):
  first_list.append(i)

print()
print(first_list)
tuple_1 = tuple(first_list)
print()
print(tuple_1)

for i in range(-5, 1):
  second_list.append(i)

print()
print(second_list)
tuple_2 = tuple(second_list)
print()
print(tuple_2)

print()
third_list = first_list + second_list
print(third_list)
tuple_3 = tuple(third_list)
print()
print(tuple_3)

print( 'Количество нулей в кортеже', tuple_3.count(0))
