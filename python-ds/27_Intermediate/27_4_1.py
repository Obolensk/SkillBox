
count = 0

class СountIterator:

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration



my_iter = СountIterator(5)
for i_elem in my_iter:
    print(i_elem)


