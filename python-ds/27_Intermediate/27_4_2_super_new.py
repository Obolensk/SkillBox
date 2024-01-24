
import random
import time
elem = 0
count_num = 1
new_count = 0

class My_list():

    def __init__(self, nums):
        self.nums = nums

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.nums):
            global new_count
            while new_count < self.nums:
                new_count += 1
                global elem
                elem += random.random()
                return elem
            else:
                raise StopIteration

count = int(input('Введите количество элементов: '))
new_list = My_list(count)


print(new_list)

for i in new_list:
    print(count_num, end='  ---  ')
    print(i)
    time.sleep(1)
    count_num += 1
