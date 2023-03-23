# TODO здесь писать код

class Kid:
    def __init__(self, name, age, calm=0, hungry=0):
        self.name = name
        self.age = age
        self.calm = calm
        self.hungry = hungry
    def kid_info(self):
        print('Имя ребенка: {}\nВозраст: {}\nСостояние спокойствия : {}\nСостояние голода : {}'.format(
            self.name, self.age, self.calm, self.hungry))
class Parent:
    def __init__(self, name, age, kids_list):
        self.name = name
        self.age = age
        self.kids_list = kids_list
    def parent_info(self):
        print('Имя родителя: {}\nВозраст: {}\nСписок детей : {}'.format(self.name, self.age, self.kids_list))
    def calm(self, kid):
        kid.calm = 1
        print()
        print('Родитель {} успокоил ребенка {}'.format(self.name, kid.name))
        print(kid.kid_info())
    def feed(self, kid):
        kid.hungry = 1
        print()
        print('Родитель {} накормил ребенка {}'.format(self.name, kid.name))
        print(kid.kid_info())



tom = Kid('Tom', 4, 0, 0)
tom.kid_info()

ivan = Parent('Ivan', 3, [tom, 'Eve', 'Pit'])
# ivan.parent_info()

ivan.calm(tom)
ivan.feed(tom)