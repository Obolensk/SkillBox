
class Toyota:

    def __init__(self, color, price, speed, cur_speed):
        self.color = color
        self.price = price
        self.speed = speed
        self.cur_speed = cur_speed

    def info(self):
        print('Car color is {}, car price is {} USD, max speed is {}, current speed is {}!'.format(
            self.color, self.price, self.speed, self.cur_speed)
        )

    def cur_speed_correct(self, new_speed):
        self.cur_speed = new_speed

hilux = Toyota('black', 250, 180, 10)

hilux.info()
hilux.cur_speed_correct(123)
hilux.info()