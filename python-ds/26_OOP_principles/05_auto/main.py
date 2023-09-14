# TODO здесь писать код

class Auto:
    def __init__(self, direction, x=0, y=0):
        # if self.direction not in ['up', 'down', 'left', 'right']:
        #     print("Ошибка, значение должно быть из списка: 'up', 'down', 'left', 'right'")
        # else:
        self.direction = direction
        self.x = x
        self.y = y

    def move(self, metres):
        print('\nАвтомобиль едет на {} метров по направлению {}'.format(metres, self.direction))
        if self.direction == 'up':
            self.y += metres
        elif self.direction == 'down':
            self.y -= metres
        elif self.direction == 'left':
            self.x -= metres
        elif self.direction == 'right':
            self.x += metres

    def turn(self, new_direction):
        print('\nНаправление движения автомобиля/автобуса сменяется с {} на {}'.format(self.direction, new_direction))
        self.direction = new_direction

    def __str__(self):
        return '\nНаправление движение автомобиля {}\nКоордината X равна {}\nКоордината Y равна {}'\
            .format(self.direction, self.x, self.y)

class Bus(Auto):
    def __init__(self, direction, passengers, rate_per_meter=0, money=0, x=10, y=10):
        super().__init__(direction, x, y)
        self.passengers = passengers
        self.rate_per_meter = rate_per_meter
        self.money = money

    def inside(self, new_passengers):
        self.passengers += new_passengers
        print('\nИз автобуса вышли {} \nВсего пассажиров в автобусе стало {}'.format(new_passengers, self.passengers))

    def outside(self, came_out):
        self.passengers -= came_out
        print('\nВ автобус вошли {} \nВсего пассажиров в автобусе стало {}'.format(came_out, self.passengers))

    def move(self, metres):
        self.money += self.passengers * self.rate_per_meter * metres
        print('\nАвтобус едет на {} метров по направлению {}\nСтавка за метр с пассажира равна {}\n'
              'Колличество пассажиров {} человек\nОбщая стоимость поездки {} рублей\nВсего денег {} рублей'
              .format(metres, self.direction, self.rate_per_meter, self.passengers,
                      self.passengers * self.rate_per_meter * metres, self.money))
        if self.direction == 'up':
            self.y += metres
        elif self.direction == 'down':
            self.y -= metres
        elif self.direction == 'left':
            self.x -= metres
        elif self.direction == 'right':
            self.x += metres

    def __str__(self):
        return '\nНаправление движение автобуса {}\nКоордината X равна {}\nКоордината Y равна {}\n' \
               'Количесво пассажиров в автобусе {}\nСтавка за метр с пассажира {}\nВсего денег у водителя {}'\
            .format(self.direction, self.x, self.y, self.passengers, self.rate_per_meter, self.money)


a = Auto('up', 5, 6)
print(a)
a.move(12)
print(a)
a.turn('right')
a.move(5)
print(a)
print()
print('Создали автобус')
b = Bus('down', x=30, y=30, passengers=2, rate_per_meter=2, money=50)
print(b)
b.move(10)
print(b)
b.turn('right')
print(b)
b.move(5)
print(b)
b.inside(10)
b.outside(5)
b.move(5)
print(b)

