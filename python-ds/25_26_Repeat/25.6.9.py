
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
        # print('board.my_board = ', board.my_board)
        # print('board.my_board.items() = ', board.my_board.items())
        # print('board.my_board.values() = ', board.my_board.values())
        # print('board.my_board.keys() = ', board.my_board.keys())
        # print(5 in board.my_board.keys())
        # print('board.my_board[step] = ', board.my_board[step])
        if step in board.my_board.keys():
            if board.my_board[step] == '':
                board.my_board[step] = self.sym
            else:
                print('The board is busy, one more step please!')
                self.make_step(board)
        else:
            print("The cell isn't in the board, one more step please")
            self.make_step(board)
        print(board.my_board)

        # self.is_winner(b)

    def game(self, board):
        # print(board.my_board.values())
        while not self.is_winner(b) == False:
            while '' in board.my_board.values():
                self.make_step(b)
                self.is_winner(b)

    def is_winner(self, board):
        winner = False
        for i in range(1, len(board.my_board)-2):
            print('i = ', i)
            print('i % 3 = ', i % 3)
            print('board.my_board[i] = ', board.my_board[i])
            print('board.my_board[i+1] = ', board.my_board[i + 1])
            print('board.my_board[i+2] = ', board.my_board[i + 2])
            if i % 3 == 1 and board.my_board[i] == board.my_board[i+1] == board.my_board[i+2] == self.sym:
                print('The player {} is winner!!!'.format(self.name))
                winner = True
                break


b = Board(9)
b.make_board()
me = Player('Me', 'X')
# me.make_step(b)
me.game(b)