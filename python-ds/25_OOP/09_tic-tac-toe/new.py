
import random

class Cell:
    def __init__(self, x='5x', y='6y'):
        self.x = x
        self.y = y
    # x = '5x'
    # y = '6y'

class Board:
    # def __init__(self):

    def new_board(self):
        cell_list = []
        for x_coord in ['a', 'b', 'c']:
            for y_coord in range(3):
                cell_list.append(x_coord + str(y_coord+1))
        My_dict = {}
        for cell in cell_list:
            My_dict[cell] = False
        return My_dict


class Player:

    def __init__(self, name):
        self.name = name

    def step(self, board=Board()):
        self.board = board
        my_step = input('Введите поле в формате a1, b3 и т.д.: ')
        if my_step in board:
            if board[my_step]== False:
                print('OK')
                board[my_step] = 'x'
                print(board)
            else:
                print('Занято!')
        else:
            print('Не работает!!!')


# Доработать этот метод, чтобы предлагал ходы пока не найдет пустое поле
    def comp_step(self, board=Board()):
        self.board = board
        co_step = ['a', 'b', 'c'][random.randint(0, 2)] + ['1', '2', '3'][random.randint(0, 2)]
        if co_step in board:
            if board[co_step]== False:
                print('OK')
                board[co_step] = 'o'
                print(board)
            else:
                self.comp_step(board)
        else:
            self.comp_step(board)








# a1 = Cell('aaa', 111)
# print(a1.x)
# print(a1.y)

me = Player('ME')
board = Board.new_board(5)
print(board)
me.step(board)