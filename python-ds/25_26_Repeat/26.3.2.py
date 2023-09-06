
class Robot:

    def __init__(self, model):
        self.model = model

class Vacuum(Robot):

    def __init__(self, model, pocket=0):
        super().__init__(model)
        self.pocket = pocket

    def operate(self, num=1):
        self.pocket += num
        print('I am cleaning the floor on {} num\nMy pocket fullness is {} now!\n'.format(num, self.pocket))

    def info(self):
        print('I am Vacuum cleaner Robot.\nMy model is {}\nMy pocket is {}\n'.format(self.model, self.pocket))

class War(Robot):

    def __init__(self, model, guns=1):
        super().__init__(model)
        self.guns = guns

    def operate(self, num=1):
        self.guns -= num
        print('I defense my object\nMy guns number is {}\n'.format(self.guns))

    def info(self):
        print('I am War Robot.\nMy model is {}\nMy guns number is {}\n'.format(self.model, self.guns))

class Submarine(War):

    def __init__(self, model, deepness=10):
        super().__init__(model)
        self.deepness = deepness

    def operate(self, num=1):
        print('I defense my object\nMy guns number is {}\n'.format(self.guns))
        print('I work in the Sea!')

    def info(self):
        print('I am War Submarine.\nMy model is {}\nMy guns number is {}\n'.format(self.model, self.guns))


w = War('wjhv321', 55)
v = Vacuum('v6968752', 44)
w.info()
v.info()
w.operate()
v.operate()
s = Submarine('s-65')
s.operate()
s.info()