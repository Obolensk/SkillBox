# TODO здесь писать код

import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Список из девяти пробелов
        self.current_winner = None # Победитель не определен

    def print_board(self): # метод печатает пустую доску
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]: # для строки из списка из трех списков по три пробела в каждом
            print('| ' + ' | '.join(row) + ' |') # печатаем каждый элемент списка и разделяем их символом "|" и ставим по такому же символу в начале и в конце каждой строки

    @staticmethod
    def print_board_numbers():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)] # создаем список из трех списков в каждом из которых числа от 0 до 8 по порядку
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |') # печатаем каждый элемент списка и разделяем их символом "|" и ставим по такому же символу в начале и в конце каждой строки

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' '] # функция возвращает список из девяти элементов, от 0 до 8

    def empty_squares(self):
        return ' ' in self.board # функция возвращает True если на доске ещё есть пустые поля

    def num_empty_squares(self):
        return self.board.count(' ') # функция возвращает количество пустых полей на доске

    def make_move(self, square, letter): # функция принимает 2 аргумента, поле и символ (крестик или нолик), если поле пустое, то делаем ход и проверяем победил ли игрок, если поле не пустое, то возвращает False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3 # row_ind = 0, 1, 2
        row = self.board[row_ind * 3: (row_ind + 1) * 3] # Проверяет три подряд элемента, начиная с элемента 0, 3, 6 (проверят строки) и возвращает True если все элементы одинаковы
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3 # col_ind = 0, 1, 2
        column = [self.board[col_ind + i * 3] for i in range(3)] # Проверяет три элемента (0,3,6 / 1,4,7 / 2,5,8) (проверят столбцы) и возвращает True если все элементы одинаковы
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # Проверяет диагональ и возвращает True если все элементы одинаковы
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False # в противном случае False


def play(game, x_player, o_player, print_game=True): # Функция вне классов, принимает на вход название игры и имена игроков,
    if print_game:
        game.print_board_numbers() # печатает доску с ходами игроков???

    letter = 'X'
    while game.empty_squares(): # если на доске ещё есть пустые поля
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print('\n' + letter + ' makes a move to square', square)
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print('It\'s a tie!')

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game): # ход игрока
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ') # предложение сделать ход
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class RandomComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)