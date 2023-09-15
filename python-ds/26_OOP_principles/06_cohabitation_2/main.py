# TODO здесь писать код

class House:
    def __init__(self, money=100, meal=50, pet_meal=30, dirt=0):
        self.money = money
        self.meal = meal
        self.pet_meal = pet_meal
        self.dirt = dirt

    def __str__(self):
        return 'House info:\n Money = {}\n Meal = {}\n Pet meal = {}\n Dirt = {}'.format\
            (self.money, self.meal, self.pet_meal, self.dirt)

class Neighbor(House):
    def __init__(self, name, satiety=30, happyness=100):
        super().__init__()
        self.name = name
        self.satiety = satiety
        self.happyness = happyness

    def eat(self):
        self.satiety += 30
        self.meal -= 30

    def earn_money(self):
        self.money += 150
        self.satiety -= 10

    def buy_the_meal(self, num):
        self.money -= num
        self.meal += num
        self.satiety -= 10

    def buy_the_pet_meal(self, num):
        self.money -= num
        self.pet_meal += num
        self.satiety -= 10

    def buy_the_coat(self):
        self.money -= 350
        self.happyness += 60
        self.satiety -= 10

    def play(self):
        self.happyness += 20
        self.satiety -= 10

    def clean(self):
        self.dirt -= 100
        self.satiety -= 10

class Human(Neighbor):
    def __init__(self, name):
        super().__init__(name)

    def pet_the_cat(self):
        self.happyness += 5
        self.satiety -= 10

class Cat(Neighbor):
    def __init__(self, name, satiety=30):
        super().__init__(name, satiety)

    def eat(self):
        self.satiety += 20
        self.pet_meal -= 10

    def tear_wallpaper(self):
        self.dirt += 5
        self.satiety -= 10

my = House()
hus = Human('Tom')
# print(my)
# print(hus)

for day in range(1, 10):
    print('\nDay nuber {}:'.format(day))
    my.dirt += 5
    print(my)


