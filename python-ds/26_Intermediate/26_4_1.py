class Unit:
    def __init__(self, health):
        self.health = health

    def damage(self, value):
        self.value = value
        self.health -= self.value
        print('Нанесен урон в размере', self.value)
        print('Остаток здоровья:', self.health)

class Soldier(Unit):
    def __init__(self, health):
        super().__init__(health)

    # def damage(self, value):
    #     self.value = value
    #     # val = input('Введите значение урона: ')
    #     # value = val

class Citizen(Unit):
    def __init__(self, health):
        super().__init__(health)

    def damage(self, value):
        self.value = value
        self.health -= self.value * 2
        print('Нанесен урон в размере', self.value * 2)
        print('Остаток здоровья:', self.health)


sol = Soldier(15)
# print(sol.health)
# sol.damage(2)
# print()
cit = Citizen(25)
# print(cit.health)
# cit.damage(2)
print()
for i in (sol, cit):
    print('Здоровье юнита'.format(i.health))
    i.damage(2)
    print()


