
class Toyota:
    color = 'red'
    price = 1000000
    speed = 200
    cur_speed = 0

    def info(self):
        print('Car color is {}, car price is {} USD, max speed is {}, current speed is {}!'.format(
            self.color, self.price, self.speed, self.cur_speed)
        )

    def cur_speed_correct(self, new_speed):
        self.cur_speed = new_speed

hilux = Toyota()

hilux.info()
hilux.cur_speed_correct(123)
hilux.info()