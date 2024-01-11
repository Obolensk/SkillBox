
import time
count = 0

def СountIterator():
    while True:
        global count
        count += 1
        print(count)
        time.sleep(0.1)

my_iter = СountIterator()
for i_elem in my_iter:
    print(i_elem)
