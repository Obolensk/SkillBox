# 9:03

import random

class Warior:

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self):
        self.health -= 20

    def info(self):
        print('Health of {} is {} points'.format(self.name, self.health))


w1 = Warior('First')
w2 = Warior('Second')

while w1.health > 0 and w2.health > 0:
    if random.randint(1, 2) == 1:
        print('\n{} was attacked by {}'.format(w2.name, w1.name))
        w2.attack()
    else:
        print('\n{} was attacked by {}'.format(w1.name, w2.name))
        w1.attack()
    w1.info()
    w2.info()

if w1.health <= 0:
    print('\nThe winner is First warrior')
else:
    print('\nThe winner is First warrior')