
import random

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

a = random.randint(0, 10)
print('a = ', a)
b = random.randint(11, 20)
print('b = ', b)

n = n[:a] + n[b:]
print(n)
