
class Human:

    count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Human.count += 1

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age in range(0, 101):
            self.__age = age
        else:
            raise Exception('Возраст должен быть от 0 до 100 лет')


ivan = Human('Ivan', 35)
# print(ivan.__name)
# print(ivan.__age)
print(ivan.count)

dima = Human('Dima', 22)
# print(dima.__name)
# print(dima.__age)
print(dima.count)

print(ivan.get_name())
print(dima.get_name())
ivan.set_name('Petr')
print(ivan.get_name())
print()
print(ivan.get_age())
ivan.set_age(100)
print(ivan.get_age())
print(Human._Human__age)
