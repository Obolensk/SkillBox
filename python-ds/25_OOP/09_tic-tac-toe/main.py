# TODO здесь писать код
class Cell:
    def __init__(self, number, value):
        self.number = number
        self.value = value
class Board(Cell):
    # def __init__(self):
        def new_cell(self):
            my_board = []
            new_one = self.value
            for i in range(9):
                my_board.append(new_one)

print(Board)
print(Board.new_cell())
# print(Cell.new_cell())

# for i in Board.new_cell():
#     print(i)
