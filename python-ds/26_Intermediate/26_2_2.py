
class Human:

    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Human.count += 1

ivan = Human('Ivan', 35)
print(ivan.name)
print(ivan.age)
print(ivan.count)

dima = Human('Dima', 22)
print(dima.name)
print(dima.age)
print(dima.count)

