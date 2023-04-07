# TODO здесь писать код
import random

class Cell:
    def __init__(self, x='5x', y='6y'):
        self.x = x
        self.y = y

class Board:
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
                self.step(board)
        else:
            print('Не работает!!!')
            self.step(board)
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

me = Player('ME')
board = Board.new_board(5)
print(board)

deal = Player('Dealer')

false_count = 9
for i in board:
    print(board[i])
    if board[i] != False:
        false_count -= 1
print(false_count)

winner = False
while false_count > 0 and winner == False:
    me.step(board)
    deal.comp_step(board)
    if board['a1'] == board['a2'] == board['a3'] == 'x' or board['a1'] == board['b2'] == board['c3'] == 'x' \
            or board['a3'] == board['b2'] == board['c1'] == 'x' or board['b1'] == board['b2'] == board['b3'] == 'x' \
            or board['c1'] == board['c2'] == board['c3'] == 'x' or board['a1'] == board['b1'] == board['c1'] == 'x' \
            or board['a2'] == board['b2'] == board['c2'] == 'x' or board['a3'] == board['b3'] == board['c3'] == 'x':
        print('Наш победитель - это пользователь по имени {}'.format(me.name))
    elif board['a1'] == board['a2'] == board['a3'] == 'o' or board['a1'] == board['b2'] == board['c3'] == 'o' \
            or board['a3'] == board['b2'] == board['c1'] == 'o' or board['b1'] == board['b2'] == board['b3'] == 'o' \
            or board['c1'] == board['c2'] == board['c3'] == 'o' or board['a1'] == board['b1'] == board['c1'] == 'o' \
            or board['a2'] == board['b2'] == board['c2'] == 'o' or board['a3'] == board['b3'] == board['c3'] == 'o':
        print('Наш победитель - это пользователь по имени {}'.format(deal.name))
        winner = True
else:
    print('Игра закончена!')


