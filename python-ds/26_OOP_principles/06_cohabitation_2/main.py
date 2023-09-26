# TODO здесь писать код

money = 100
meal = 50
pet_meal = 30
dirt = 0
human_list = []
pet_list = []
coat = 0
earned_money = 0
eated_meal = 0

# def house_info:
#     print()

class Neighbor:
    def __init__(self, name, satiety=30):
        self.name = name
        self.satiety = satiety

    def eat(self):
        print('\n{} is hungry. Try to eat'.format(self.name))
        self.satiety += 30
        global meal
        meal -= 30
        global eated_meal
        eated_meal += 30
        print(self)

    def __str__(self):
        return '\nMy name is {}\nMy satiety is {}\nMeal in my house is {}\nPet meal in my house is {}\n' \
               'Dirt in my house is {}'.format(self.name, self.satiety, meal, pet_meal, dirt)

class Human(Neighbor):
    def __init__(self, name, happyness=100):
        super().__init__(name)
        self.happyness = happyness
        human_list.append(self)

    def play(self):
        self.satiety -= 10
        self.happyness += 20
        print(self)

    def pet_the_cat(self):
        self.happyness += 5
        self.satiety -= 10

    def clean(self):
        print('\nThere is too dirty!\nThe wife {} is cleaning'.format(self.name))
        global dirt
        dirt -= 100
        self.satiety -= 10
        self.happyness -= 20
        print(self)

    def earn_money(self):
        global money
        money += 150
        global earned_money
        earned_money += 150
        self.happyness -= 50
        self.satiety -= 10
        print('\nSidney earned some money')

    def buy_the_meal(self, num):
        global money
        money -= num
        global meal
        meal += num
        print('\nSteve buy the meal')

    def buy_the_pet_meal(self, num):
        global money
        money -= num
        global pet_meal
        pet_meal += num
        print('\nSteve buy the pet meal')

    def buy_the_coat(self):
        global money
        money -= 350
        global coat
        coat += 1
        self.happyness += 60
        self.satiety -= 10
        print("\n{} buy the coat\nMoney is {}\n{}'s happiness is {}".format(self.name, money, self.name,
                                                                            self.happyness))
    def __str__(self):
        return '\nMy name is {}\nMy satiety is {}\nMy happiness is {}\nMeal in my house is {}\nPet meal in my house ' \
               'is {}\nDirt in my house is {}'.format(self.name, self.satiety, self.happyness, meal, pet_meal, dirt)

class Pet(Neighbor):
    def __init__(self, name):
        super().__init__(name)
        pet_list.append(self)

    def eat(self):
        self.satiety += 20
        global pet_meal
        pet_meal -= 10

    def __str__(self):
        return '\nMy name is {}\nMy satiety is {}\nPet meal in my house ' \
               'is {}\nDirt in my house is {}'.format(self.name, self.satiety, pet_meal, dirt)

sid = Human('Sidney')
nan = Human('Nancy')
tom = Pet('Tom')
# print(sid)
# print(tom)
# nan.buy_the_coat()
# sid.eat()
# tom.eat()
# sid.play()
# print(sid)
# print(tom)

for day in range(1, 366):
    print('\nDay №', day)
    dirt += 5
    # print(' Dirty level is', dirt)
    if dirt >= 100:
        nan.clean()
    if meal <= 60:
        sid.buy_the_meal(200)
    for human in human_list:
        human.satiety -= 20
        if human.satiety <= 20:
            human.eat()
        if human.happyness <= 10:
            if human.name == 'Sidney':
                human.play()
            else:
                if money >= 350:
                    human.buy_the_coat()
                else:
                    sid.earn_money()
                    human.buy_the_coat()

print('\nAll my coats are {}\nAll meal was eated are {}\nAll money was earned are {}'.format(coat, meal, earned_money))


