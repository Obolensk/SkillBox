
import time
count = 0

class СountIterator():

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            global count
            count += 1
            print(count)
            time.sleep(0.1)

my_iter = СountIterator()
for i_elem in my_iter:
    print(i_elem)
