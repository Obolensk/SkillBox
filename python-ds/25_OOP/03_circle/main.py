# TODO здесь писать код

import math
class Circle:
    def __init__(self, name, x=0, y=0, r=1):
        self.name = name
        self.x = x
        self.y = y
        self.r = r
    def square(self):
        s = math.pi * (self.r ** 2)
        print('Площадь круга равняется {}'.format(s))
    def long(self):
        l = 2 * math.pi * self.r
        print('Длина окружности: {}'.format(l))
    def increase(self, k):
        self.r *= k
        self.square()
        self.long()

all_circles = []
first = Circle('first', 0, 0, 3)
all_circles.append(first)
second = Circle('second', 2, 3, 3)
all_circles.append(second)
third = Circle('third', 5, 6, 2)
all_circles.append(third)
print()
for a in all_circles:
    for b in all_circles:
        if a != b:
            d = math.sqrt(abs(a.x - b.x) ** 2 + abs(a.y - b.y) ** 2)
            if d > a.r + b.r:
                print('Круги {} и {} не пересекаются!'.format(a.name, b.name))
            else:
                print('Круги {} и {} пересекаются!'.format(a.name, b.name))
        else:
            continue
    all_circles.pop(all_circles.index(a))
