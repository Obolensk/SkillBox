# TODO здесь писать код

money = 100
meal = 50
pet_meal = 30
dirt = 0

class Neighbor:
    def __init__(self, name, satiety=30):
        self.name = name
        self.satiety = satiety

    def eat(self):
        self.satiety += 30
        global meal
        meal -= 30

    def __str__(self):
        return '\nMy name is {}\nMy satiety is {}\nMeal in my house is {}\nPet meal in my house is {}\n' \
               'Dirt in my house is {}'.format(self.name, self.satiety, meal, pet_meal, dirt)

class Human(Neighbor):
    def __init__(self, name, happyness=100):
        super().__init__(name)
        self.happyness = happyness

    def play(self):
        self.satiety -= 10
        self.happyness += 20

    def pet_the_cat(self):
        self.happyness += 5
        self.satiety -= 10

    def earn_money(self):
        global money
        money += 150
        self.happyness -= 20
        self.satiety -= 10
        print('\nSidney earned some money')

    def buy_the_coat(self):
        global money
        money -= 350
        self.happyness += 60
        self.satiety -= 10
        print("\nNancy buy the coat\nMoney is {}\n{}'s happiness is {}".format(self.name))

        # print('Buy the coat.\nI have {} coats'.format(coat))


    def __str__(self):
        return '\nMy name is {}\nMy satiety is {}\nMy happiness is {}\nMeal in my house is {}\nPet meal in my house is {}\n' \
               'Dirt in my house is {}'.format(self.name, self.satiety, self.happyness, meal, pet_meal, dirt)

class Pet(Neighbor):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        self.satiety += 20
        global pet_meal
        pet_meal -= 10

sid = Human('Sidney')
nan = Human('Nancy')
tom = Pet('Tom')
print(sid)
print(tom)
sid.eat()
tom.eat()
print(sid)
print(tom)