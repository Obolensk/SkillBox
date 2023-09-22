# TODO здесь писать код

human_list = []
pet_list = []
coat = 0
num_of_play = 0

class House:
    def __init__(self, money=100, meal=50, pet_meal=30, dirt=0):
        self.money = money
        self.meal = meal
        self.pet_meal = pet_meal
        self.dirt = dirt

    def buy_the_meal(self, num):
        self.money -= num
        self.meal += num
        print('\nSteve buy the meal')

    def buy_the_pet_meal(self, num):
        self.money -= num
        self.pet_meal += num
        print('\nSteve buy the pet meal')

    def __str__(self):
        return 'House info:\n  Money = {}\n  Meal = {}\n  Pet meal = {}\n  Dirt = {}'.format\
            (self.money, self.meal, self.pet_meal, self.dirt)

class Neighbor(House):
    def __init__(self, name, money=100, satiety=30, happyness=100):
        super().__init__()
        self.name = name
        # self.house = house
        self.money = money
        self.satiety = satiety
        self.happyness = happyness

    def pet_the_cat(self):
        self.happyness += 5
        self.satiety -= 10

    def earn_money(self):
        self.money += 150
        self.happyness -= 20
        self.satiety -= 10
        print('\nSteve earned money')

    def buy_the_coat(self):
        self.money -= 350
        self.happyness += 60
        self.satiety -= 10
        print('Buy the coat.\nI have {} coats'.format(coat))

    def play(self):
        self.happyness += 20
        self.satiety -= 10
        print('I played {}-th times'.format(num_of_play))

    def clean(self):
        print('\nThere is too dirty!\nThe wife {} is cleaning'.format(self.name))
        self.dirt -= 100
        self.satiety -= 10
        self.happyness -= 40

    def eat(self):
        self.satiety += 30
        self.meal -= 30
        self.happyness += 30
        print('\n{} eat'.format(self.name))

    def __str__(self):
        return '\nMy name is {}\nMy satiety is {}\nMy happiness level is {}'\
            .format(self.name, self.satiety, self.happyness)

class Cat(Neighbor):
    def __init__(self, name, house=0, money=0, satiety=30):
        super().__init__(name, house, money, satiety)
        self.house = house
        self.money = money
        pet_list.append(self)

    def eat(self):
        self.satiety += 20
        self.pet_meal -= 10
        print('\n{} eat'.format(self.name))

    def tear_wallpaper(self):
        self.dirt += 5
        self.satiety -= 10
        print('\n{} tear wallpaper'.format(self.name))

    def __str__(self):
        return '\nMy name is {}\nI am a cat\nMy satiety is {}\nMy happiness level is {}'\
            .format(self.name, self.satiety, self.happyness)

my = House()
hus = Neighbor('Steve')
wife = Neighbor('Eve')
cat = Cat('Tom')
print(my)
print(hus)


for day in range(1, 365):
    print('******************************')
    print('\nDay nuber {}:'.format(day))
    my.dirt += 5
    print(my)
    print(hus)
    print(wife)
    print(cat)
    for pet in pet_list:
        pet.satiety -= 15
        if pet.satiety < 10:
            pet.eat()
            my.pet_meal -= 10
    for human in human_list:
        human.happyness -= 10
        human.satiety -= 15
        if human.satiety <= 15:
            human.eat()
            my.meal -= 30
    if my.dirt >= 100:
        wife.clean()
        my.dirt -= 100
    if wife.happyness <= 20:
        wife.buy_the_coat()
        coat += 1
    if hus.happyness <= 20:
        hus.play()
        num_of_play += 1
    if my.meal <= 20:
        my.buy_the_meal(20)
    if my.pet_meal <= 10:
        my.buy_the_pet_meal(10)
    if my.money <= 50:
        hus.earn_money()


#
# print(Human.__getattribute__(hus, name='Tom'))
# print(hus)
# print(wife)
# print(my.dirt)
# print()
# print(human_list)

