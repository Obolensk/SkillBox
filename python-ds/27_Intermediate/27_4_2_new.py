
import random
elem = 0
count_num = 1
def my_list(nums):
    for i in range(nums):
        global elem
        elem += random.random()
        yield elem

count = int(input('Введите количество элементов: '))

print(my_list(count))

for i in my_list(count):
    print(count_num, end='  ---  ')
    print(i)
    count_num += 1
