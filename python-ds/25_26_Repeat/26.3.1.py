
class Ship:

    def __init__(self, model):
        self.model = model

    def info(self):
        print('The ship model is {}'.format(self.model))
        # ship_info(self)


class Cargo(Ship):

    def __init__(self, model, fullness=0):
        super().__init__(model)
        self.fullness = fullness

    def load(self, nums):
        self.fullness += nums
        print('The {} ship was loaded on {} nums\nTotal cargo is {} now!\n'.format(self.model, nums, self.fullness))

    def unload(self, nums):
        self.fullness -= nums
        print('The {} ship was unloaded on {} nums\nTotal cargo is {} now!\n'.format(self.model, nums, self.fullness))

    def info(self):
        print('The ship {} is cargo ship\nIt has {} fullness\n'.format(self.model, self.fullness))

class War(Ship):

    def __init__(self, model, guns):
        super().__init__(model)
        self.guns = guns

    def attack(self):
        self.guns -= 1
        print('The {} ship attack!!!\nThe guns remain is {}\n'.format(self.model, self.guns))

    def info(self):
        print('The ship {} is war ship\nIt has {} guns!\n'.format(self.model, self.guns))


w = War('w21', 5)
c = Cargo('c87')
w.info()
c.info()
c.load(44)
c.info()
c.unload(10)
c.info()