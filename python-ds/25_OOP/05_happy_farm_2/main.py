class Gardener:
    ...

class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.name = 'картошка'
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.state]}')


class Gardenbed:
    ...


my_garden = Gardenbed(5)
my_garden.are_all_ripe()
my_gardener = Gardener(name='Боря', garden_bed=my_garden)
my_gardener.take_care_garden_bed()
my_gardener.about_me()
my_gardener.take_care_garden_bed()
my_gardener.harvest()
my_gardener.about_me()

