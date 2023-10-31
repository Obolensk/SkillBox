
def СountIterator():
    count = 1
    while True:
        print(count)
        count += 1

my_iter = СountIterator()
for i_elem in my_iter:
    print(i_elem)
