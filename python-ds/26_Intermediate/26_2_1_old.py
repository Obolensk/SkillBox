
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
        # return f"Координата точки Х = {self.x}, координата У = {self.y}"
        return 'Координата точки Х = {}, координата Y = {}'.format(self.__x, self.__y)

    def get_x(self):


a = Point(2, 43)
b = Point(5, 12)
# a.info()

print(str(a))
print()
print(str(b))


# print(a.count)
# print(b.count)

