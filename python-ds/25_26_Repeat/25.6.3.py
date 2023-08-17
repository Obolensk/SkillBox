
import math

class Circle:

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def square(self):
        s = self.r ** 2 * math.pi
        print(s)

    def per(self):
        p = self.r * 2 * math.pi
        print(p)

    def incr(self, k):
        self.r *= k
        self.square()
        self.per()

    def inter(self, x1, y1, r1):
        k1 = abs(self.x - x1)
        print(k1)
        k2 = abs(self.y - y1)
        print(k2)
        dist = math.sqrt(k1**2 + k2**2)
        print(dist)
        if dist <= self.r + r1:
            print('Окружности пересекаются!')
        else:
            print('Окружности НЕ пересекаются!')

c1 = Circle()
c1.square()
c1.per()
c1.incr(2)

c1.square()
print()
print(c1.r)
print()

c1.inter(2, 3, 2)


