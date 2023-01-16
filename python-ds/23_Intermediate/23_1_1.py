import os

abs_path = os.path.abspath("Desktop/test.txt")
# abs_path = os.path.abspath(".")
my_path = os.path.relpath('Desktop/test.txt', '..')

print(abs_path)
print(my_path)

