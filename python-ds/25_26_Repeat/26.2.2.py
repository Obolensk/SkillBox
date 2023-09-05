
class Human:
    __count = 0
    def __init__(self, __name, __age):
        self.__name = __name
        self.__age = __age
        Human.__count += 1

    def __str__(self):
        print("Human's name is {}\nand Age is {}".format(self.__name, self.__age))
        print(self.__count)

    def get_name(self):
        print('The name of Human is', self.__name)

    def get_age(self):
        print('The Age of Human is', self.__age)

    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        self.__age = new_age

tom = Human('Tom', 25)
tom.__str__()
print()
tom.get_name()
tom.get_age()
tom.set_name('Dima')
tom.get_name()
tom.set_age(12)
tom.get_age()
tom.__str__()
