import random


class Toyota:
    color = 'red'
    price = 1000000
    speed = 200
    cur_speed = 0

print(Toyota.color)

Hilux = Toyota()
camry = Toyota()
venzo = Toyota()


Hilux.cur_speed = random.randint(0, 200)
camry.cur_speed = random.randint(0, 200)
venzo.cur_speed = random.randint(0, 200)
print(Hilux.cur_speed)
print(camry.cur_speed)
print(venzo.cur_speed)