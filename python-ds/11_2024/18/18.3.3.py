
import random

first = [random.randint(50, 80) for _ in range(10)]
second = [random.randint(30, 60) for _ in range(10)]
third = ['Погиб' if first[i] + second[i] > 100 else 'Выжил' for i in range(10)]

print(first)
print(second)
print(third)