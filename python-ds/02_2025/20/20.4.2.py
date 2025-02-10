import random


nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]

nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

# nums_1.extend(nums_2)
nums_3 = nums_1 + nums_2

# print(set(nums_3))
# print(nums_3)

print()
print('1-е множество: ', set(nums_1))
print('2-е множество: ', set(nums_2))
min_1 = min(nums_1)
min_2 = min(nums_2)

print('\nМинимальный элемент 1-го множества: ', min_1)
print('Минимальный элемент 2-го множества: ', min_2)
#

nums_1.remove(min_1)
nums_2.remove(min_2)

#

my_set_1 = set(nums_1)
my_set_2 = set(nums_2)

if min_1 in my_set_1:
    my_set_1.remove(min_1)
if min_2 in my_set_2:
    my_set_2.remove(min_2)
#
ran_1 = random.randint(100, 200)
ran_2 = random.randint(100, 200)

print('\nСлучайное число для 1-го множества: ', ran_1)
print('Случайное число для 2-го множества: ', ran_2)
my_set_1.add(ran_1)
my_set_2.add(ran_2)
#
print('\n1-е множество: ', set(my_set_1))
print('2-е множество: ', set(my_set_2))

my_set_3 = my_set_1.union(my_set_2)
print('Объединение множеств: ', my_set_3)

my_set_4 = my_set_1.intersection(my_set_2)
print('Пересечение множеств: ', my_set_4)

my_set_5 = my_set_2.difference(my_set_1)
print('Элементы, входящие в nums_2, но не входящие в nums_1: ', my_set_5)






