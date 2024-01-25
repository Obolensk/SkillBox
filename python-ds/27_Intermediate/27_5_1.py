
import time

def gen():
    count = 0
    while True:
        yield count
        count += 1

for i in gen():
    print(i)
    time.sleep(0.3)
