
class Potato:

    def __init__(self, index, stage=0):
        self.index = index
        self.stage = stage

    def info(self):
        print('Potato {}-th stage is: {}'.format(self.index, self.stage))

    def grow(self):
        if self.stage < 4:
            self.stage += 1
            print('\nPotato {}-th growed on one stage'.format(self.index))
            self.info()
        else:
            print('Potato {}-th growed at ALL!'.format(self.index))

class PotatoGarden:

    def __init__(self, count):
        self.count = count
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('\nКартошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()
        self.info()

    def info(self):
        # print(self.potatoes[0].stage)
        print('\nThere are {} potatoes on the Garden\nTheir stage are {}-th'.format(self.count, self.potatoes[0].stage))

class Gardener:

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden

    def take_care(self, garden):
        print('\n{} take care for the garden which have {} potatoes'.format(self.name, garden.count))
        garden.grow_all()

    def harvest(self, garden):
        print('\n{} harvest from the garden which had {} potatoes'.format(self.name, garden.count))
        garden.count = 0
        for i in garden.potatoes:
            i.stage = 0
        garden.info()

pg = PotatoGarden(3)
tom = Gardener('Tom', pg)

while pg.potatoes[0].stage < 4:
    tom.take_care(pg)

tom.harvest(pg)



