
class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.count += 1

    def info(self):
        print('\nX = {}\nY = {}'.format(self.x, self.y))
        print('Count = {}'.format(self.count))

p1 = Point(5, 12)
p1.info()
p2 = Point(2, 3)
p2.info()
p3 = Point(7, 8)
p3.info()