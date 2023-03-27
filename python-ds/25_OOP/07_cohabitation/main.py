# TODO здесь писать код

import random

day_num = 0
class Human:
    def __init__(self, name, hungry=50, meal=50, money=0):
        self.name = name
        self.hungry = hungry
        self.meal = meal
        self.money = money
    def eat(self):
        print()
        print('{} ест!'.format(self.name))
        self.hungry += 10
        self.meal -= 10
        self.info()
    def work(self):
        print()
        print('{} работает!'.format(self.name))
        self.hungry -= 10
        self.money += 10
        self.info()
    def play(self):
        print()
        print('{} играет!'.format(self.name))
        self.hungry -= 10
        self.info()
    def shopping(self):
        print()
        print('{} пошел в магазин!'.format(self.name))
        self.meal += 10
        self.money -= 10
        self.info()
    def info(self):
        print('День номер: {}'.format(day_num))
        print('Человек по имени {}:\n  Cытость: {}\n  Еда в холодильнике: {}\n  Деньги в тумбочке: {}'
              .format(self.name, self.hungry, self.meal, self.money))

petr = Human('Петя')
petr.info()


while petr.hungry >= 0:
    day_num += 1
    cube = random.randint(1, 6)
    print(cube)
    if petr.hungry < 20:
        petr.eat()
    elif petr.meal < 10:
        petr.shopping()
    elif petr.money < 50:
        petr.work()
    elif cube == 1:
        petr.work()
    elif cube == 2:
        petr.eat()
    else:
        petr.play()
else:
    print('Очень жаль, но сытость человека по имени {} составляет {} баллов, а это значит, он умер!'.format(petr.name, petr.hungry))



