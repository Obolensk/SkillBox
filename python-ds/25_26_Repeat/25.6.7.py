
import random

class Human:
    def __init__(self, name, home, hungry=50):
        self.name = name
        self.home = home
        self.hungry = hungry

    def eat(self):
        print('   I EAT')
        self.hungry += 20
        self.home.meal -= 20

    def work(self):
        print('   I WORK')
        self.hungry -= 20
        self.home.money += 15

    def play(self):
        print('   I PLAY')
        self.hungry -= 20

    def shopping(self):
        print('   I HAVE SHOPPING')
        self.home.money -= 10
        self.home.meal += 10

    def human_info(self):
        print('\nHi, my name is {}\nIn my home I have:\n  - {} meal,\n  - {} money\nMy hungry level is {}\n\n'.format(
            self.name, self.home.meal, self.home.money, self.hungry))

class Home:

    def __init__(self, meal=50, money=0):
        self.meal = meal
        self.money = money

    def home_info(self):
        print('\n  There is {} meal in my Home\n  There is {} money in my Home'.format(self.meal, self.money))

my_home = Home()

li = Human('Li', my_home)
li.human_info()
day = 1
while li.hungry > 0:
    print('Day {}-th!'.format(day))
    day += 1
    cube = random.randint(1, 6)
    print('   There is a {} - number on the Cube'.format(cube))
    if li.hungry < 20:
        li.eat()
        li.human_info()
    else:
        if li.home.meal < 10:
            li.shopping()
            li.human_info()
        else:
            if li.home.money < 50:
                li.work()
                li.human_info()
            else:
                if cube == 1:
                    li.work()
                    li.human_info()
                else:
                    if cube == 2:
                        li.eat()
                        li.human_info()
                    else:
                        li.play()
                        li.human_info()
    # elif li.home.meal < 10:
    #         li.shopping()
    #         li.human_info()
    # elif li.home.money < 50:
    #         li.work()
    #         li.human_info()
    # elif cube == 1:
    #         li.work()
    #         li.human_info()
    # elif cube == 2:
    #         li.eat()
    #         li.human_info()
    # else:
    #     li.play()
    #     li.human_info()
print()
print("I'm so sorry. {} died!!!".format(li.name))
