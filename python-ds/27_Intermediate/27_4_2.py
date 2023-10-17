
import random

count = int(input('Ведите количество элементов: '))
elem = 0
def gen(num):
    for i in range(num):
        global elem
        elem += random.random()
        print(elem)

gen(count)
