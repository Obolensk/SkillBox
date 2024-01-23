

count = 0

def СountIterator():
    while True:
        global count
        count += 1
        print(count)

my_iter = СountIterator()
for i_elem in my_iter:
    print(i_elem)


