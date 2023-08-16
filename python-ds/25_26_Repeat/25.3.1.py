
import random

class Citroen:
    color = 'black'
    price = 10 ** 6
    max_speed = 200
    current_speed = 0

    def print_info(self):
        print('Информация об объекте')
        print('Color is: {}\nPrice is: {}\nMax speed is: {}\nCurrent speed is: {}\n'.format(
            self.color, self.price, self.max_speed, self.current_speed))

    def set_speed(self):
        self.current_speed = int(input('Введите текущую скорость:'))

c3 = Citroen()
c4 = Citroen()
c5 = Citroen()

c3.current_speed = random.randint(0, 200)
c4.current_speed = random.randint(0, 200)
c5.current_speed = random.randint(0, 200)

print(c3.current_speed)
print(c4.current_speed)
print(c5.current_speed)

c3.print_info()
c4.print_info()
c5.print_info()

print()
c3.set_speed()
c3.print_info()