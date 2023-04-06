# TODO здесь писать код

class Cell:
    def __init__(self, number=0, value=False):
        self.number = number
        self.value = value
    def step(self):
        if self.value == True:
            print('Клетка {} занята'.format(self.number))
        else:
            self.value = True

class Board():
    def cells(self, cell):
        self.cell = cell
        cell = Cell()
        my_board = []
        for i in range(9):
            my_board.append(Cell(number=i, value=False))
            print('Номер - {} Значение - {}'.format(cell.number, cell.value))
        # return my_board

class Player:
    def __init__(self, name, step=False):
        self.name = name
        self.step = step

me = Player('I am')
print(me.name)
me.step = 'x'
print(me.step)
cell = Cell(1)
bbb = Board()
bbb.cells(cell)
# print(bbb.cells())

# for a in bbb.cells():
#     for i in a:
#         print(i)


# print('Номер - {} Значение - {}'.format(cell.number, cell.value))