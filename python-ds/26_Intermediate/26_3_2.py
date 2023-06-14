
class Robot:

    def __init__(self, model):
        self.model = model

    def operate(self):
        print('\nЯ работаю!')

class Vacuum(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.bag = 0

    def operate(self):
        print('\nЯ пылесошу пол!')
        self.bag += 1
        print('\nТекущая заполняемость мешка', self.bag)

class War(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.gun = 'MyGuns'

    def operate(self):
        print('\nЯ защищаю военный объект с помощью оружия', self.gun)


class Submarine(War):
    def __init__(self, model, deep):
        super().__init__(model)
        self.deep = deep

    def operate(self):
        print('\nЯ защищаю военный объект с помощью оружия', self.gun)
        print('\nОхрана ведется под водой!')


vac = Vacuum('v1')
wa = War('w12')
su = Submarine('su87', 12)

vac.operate()
wa.operate()
su.operate()



