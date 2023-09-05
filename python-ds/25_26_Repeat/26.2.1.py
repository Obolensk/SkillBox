
class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.count += 1

    def info(self):
        print('\nX = {}\nY = {}'.format(self.x, self.y))
        print('Count = {}'.format(self.count))


    def __str__(self):
        return self.info()

    def set_x(self):
        new_x = int(input('Введите новое значение Х: '))
        self.x = new_x

    def get_x(self):
        print('Значение Х равно', self.x)


    def set_y(self):
        new_y = int(input('Введите новое значение Y: '))
        self.y = new_y

    def get_y(self):
        print('Значение Y равно', self.y)


p1 = Point(5, 12)
p1.info()
p2 = Point(2, 3)
# p2.info()
p3 = Point(7, 8)
# p3.info()


p1.__str__()
p1.set_x()
p1.__str__()
p1.get_x()
p1.__str__()
p1.set_y()
p1.__str__()
p1.get_y()
p1.__str__()