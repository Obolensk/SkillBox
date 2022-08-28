
import random

N = random.randint(5, 15)
print('N = ', N)
print()

A = random.randint(0, N-1)
print('A = ', A)
print()

B = random.randint(A, N-1)
print('B = ', B)
print()

list = [random.randint(-100, 100) for _ in range(N)]
print('list = ', list)
print()

new_list = list[0:A] + list[B+1:-1]
print('new_list = ', new_list)