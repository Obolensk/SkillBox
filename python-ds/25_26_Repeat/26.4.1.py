
class Unit:
    def __init__(self, hitpoint):
        self.hitpoint = hitpoint

    def get_loss(self):
        self.hitpoint -= 0

    def __str__(self):
        return '\nUnit {}\nHipoint is {}\nLoss is {}'.format(1, self.hitpoint, self.loss)


class Soldier(Unit):

    def __init__(self, loss, hitpoint):
        super().__init__(hitpoint)
        self.loss = loss

    def get_loss(self):
        self.hitpoint -= self.loss

    # def __str__(self):
    #     return 'Unit {}\nHipoint is {}\nLoss is {}'.format(1, self.hitpoint, self.loss)

class Citizen(Unit):
    def __init__(self, loss, hitpoint):
        super().__init__(hitpoint)
        self.loss = loss

    def get_loss(self):
        self.hitpoint -= self.loss * 2

s = Soldier(2, 10)
print(s)
s.get_loss()
print(s)
c = Citizen(3, 20)
print(c)
c.get_loss()
print(c)



