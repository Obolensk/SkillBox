
class Potato:

    def __init__(self, index, stage=0):
        self.index = index
        self.stage = stage

    def info(self):
        print('Potato {}-th stage is: {}'.format(self.index, self.stage))

    def grow(self):
        if self.stage < 4:
            self.stage += 1
            print('Potato {}-th growed on one stage'.format(self.index))
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

pg = PotatoGarden(12)

pg.grow_all()
pg.grow_all()
pg.grow_all()
pg.grow_all()
pg.grow_all()
