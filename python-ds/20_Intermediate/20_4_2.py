import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

# print()
# print(nums_1)
# print()
# print(nums_2)

nums_1 = set(nums_1)
nums_2 = set(nums_2)

print()
print('1-е множество: ', nums_1)
print()
print('2-е множество: ', nums_2)

print()

print('Минимальный элемент 1-го множества:', min(nums_1))
print('Минимальный элемент 2-го множества:', min(nums_2))

r_1 = random.randint(100, 200)
r_2 = random.randint(100, 200)

nums_1.add(r_1)
nums_2.add(r_2)


# print()
# print('1-е множество: ', nums_1)
# print()
# print('2-е множество: ', nums_2)

print()
print('Случайное число для 1-го множества: ', r_1)
print('Случайное число для 2-го множества: ', r_2)


    # Вывести все элементы множеств (объединение).
    # Вывести только общие элементы (пересечение).
    # Вывести элементы, входящие в nums_2, но не входящие в nums_1.


print()
print('Объединение множеств:', nums_1.union(nums_2))

print()
print('Пересечение множеств:', nums_1.intersection(nums_2))
# print(nums_2.intersection(nums_1))

print()
print('Элементы, входящие в nums_2, но не входящие в nums_1: ', nums_2 - nums_1)
