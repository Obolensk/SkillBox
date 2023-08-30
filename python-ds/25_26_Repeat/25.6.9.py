
class Board:

    def __init__(self, n, my_board = dict()):
        self.n = n
        self.my_board = my_board

    def make_board(self):
        for i in range(1, self.n+1):
            self.my_board[i] = ''
            if i % 3 == 0:
                print('| {} |'.format(i))
            else:
                print('| {} '.format(i), end='')
        print(self.my_board)

class Player:

    def __init__(self, name, sym):
        self.name = name
        self.sym = sym

    def make_step(self, board):
        step = int(input('Print number of cell: '))
        print('board.my_board = ', board.my_board)
        print('board.my_board.items() = ', board.my_board.items())
        print('board.my_board.values() = ', board.my_board.values())
        print('board.my_board.keys() = ', board.my_board.keys())
        if board.my_board[step] in board.my_board.keys():
            if board.my_board[step] == '':
                board.my_board[step] = self.sym
            else:
                print('The board is busy, one more step please!')
                self.make_step(board)
        else:
            print("The cell isn't in the board, one more step please")
            self.make_step(board)
        print(board.my_board)



b = Board(9)
b.make_board()
# print(b.make_board())
me = Player('Me', 'X')
me.make_step(b)