class Point:
    __x = 0
    __y = 0
    count = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        Point.count += 1

    def info(self):
        print()
        print('The point coordinates are X = {}, Y = {} \nNum of points is {}'.format(
            self.__x, self.__y, self.count
        ))

    def __str__(self):
        return 'Координата точки Х = {}, координата Y = {}'.format(self.__x, self.__y)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

a = Point(2, 3)
b = Point(5, 12)

print(str(a))
print()
print(str(b))
