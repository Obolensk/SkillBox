class Point:
    x = 0
    y = 0
    count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.count += 1

    def info(self):
        print()
        print('The point coordinates are X = {}, Y = {} \nNum of points is {}'.format(
            self.x, self.y, self.count
        ))

a = Point(2, 3)
b = Point(5, 12)
a.info()
# print(a.count)
# print(b.count)