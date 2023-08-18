
class Parent:

    def __init__(self, name, age, kids_list):
        self.name = name
        self.age = age
        self.kids_list = kids_list

    def info(self):
        for i in self.kids_list:
            if isinstance(i, Kid):
                print('\nMy name is {}\nMy age is {}\nI have kids: {}'.format(self.name, self.age, i.kid_name))
        else:
            print('\nMy name is {}\nMy age is {}\nI have kids: {}'.format(self.name, self.age, self.kids_list))

    def kid_calm(self, kid):
        print('\n{} calmed by his parent {}'.format(kid.kid_name, self.name))
        kid.stress -= 1
        kid.info()

    def kid_feed(self, kid):
        print('\n{} feeded by his parent {}'.format(kid.kid_name, self.name))
        kid.hungry -= 1
        kid.info()


class Kid:

    def __init__(self, kid_name, age, stress=0, hungry=0):
        self.kid_name = kid_name
        self.age = age
        self.stress = stress
        self.hungry = hungry

    def info(self):
        print('\nMy name is {}\nMy age is {}\nMy stress level: {}\nMy hungry level {}'.format(
            self.kid_name, self.age, self.stress, self.hungry))

tommy = Kid('Tommy', 8, 1, 2)
tommy.info()
jerry = Kid('Jerry', 12, 2, 6)
jerry.info()

sara = Parent('Sara', 44, [tommy.kid_name, jerry.kid_name])
sara.info()
sara.kid_feed(tommy)
sara.kid_calm(jerry)
