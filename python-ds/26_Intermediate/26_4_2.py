
class CanFly:
    def __init__(self, high, speed):
        self.high = high
        self.speed = speed

    def take_off(self):
        pass

    def fly(self):
        pass

    def landing(self):
        self.high = 0
        self.speed = 0
        self.info()

    def info(self):
        print('Высота равна:', self.high)
        print('Скорость равна:', self.speed)
        print('------------------------------')

class ButterFly(CanFly):
    def __init__(self, high, speed):
        super().__init__(high, speed)

    def take_off(self):
        self.high = 1
        self.speed = 0.5
        print()
        print('Бабочка ВЗЛЕТЕЛА!')
        self.info()

    def fly(self):
        self.high = 1
        self.speed = 0.5
        print()
        print('Бабочка ЛЕТИТ!')
        self.info()

class Rocket(CanFly):
    def __init__(self, high, speed):
        super().__init__(high, speed)

    def take_off(self):
        self.high = 500
        self.speed = 1000
        print()
        print('Ракета ВЗЛЕТЕЛА!')
        self.info()

    def landing(self):
        self.high = 0
        self.speed = 0
        print()
        print('Ракета ПРИЗЕМЛИЛАСЬ!')
        print('BOOOM!!!')
        self.info()




but = ButterFly(0, 0)
but.take_off()
but.fly()

r = Rocket(0, 0)
r.take_off()
r.landing()



