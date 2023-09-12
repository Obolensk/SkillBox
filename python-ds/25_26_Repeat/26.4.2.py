
class CanFly:
    def __init__(self, high=0, speed=0):
        self.high = high
        self.speed = speed

    def take_off(self):
        pass

    def fly(self):
        pass

    def landing(self):
        self.high = 0
        self.speed = 0

    def __str__(self):
        return '\nHigh is {}\nSpeed is {}'.format(self.high, self.speed)

class Butterfly(CanFly):
    def __init__(self):
        super().__init__()

    def take_off(self):
        self.high = 1
        print('\nБабочка взлетела!')

    def fly(self):
        self.speed = 0.5
        print('\nБабочка летит!')

class Rocket(CanFly):
    def __init__(self):
        super().__init__()

    def take_off(self):
        self.high = 500
        self.speed = 1000
        print('\nРакета взлетела!')

    def landing(self):
        self.high = 0
        self.speed = 0
        print('\nРакета приземлилась!\nВзрыв!')

bf = Butterfly()
print(bf)
bf.take_off()
bf.fly()
r = Rocket()
print(r)
r.take_off()
r.landing()
print(r)