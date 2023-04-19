import random  # импортируем модуль random для генерации случайных ходов


# определяем класс игры "Крестики-нолики"
class TicTacToe:
    def __init__(self):
        # инициализируем игровое поле с пустыми клетками
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # победитель - никто, пока нет игрока, который выиграл

    def print_board(self):
        # выводим игровое поле на экран
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_numbers():
        # выводим игровое поле на экран с номерами клеток
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # возвращаем список возможных ходов
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        # проверяем, есть ли на поле пустые клетки
        return ' ' in self.board

    def num_empty_squares(self):
        # возвращаем количество пустых клеток на поле
        return self.board.count(' ')

    def make_move(self, square, letter):
        # делаем ход, обновляя поле переданным символом
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # проверяем, есть ли победитель
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


# определяем функцию, которая будет запускать игру
def play(game, x_player, o_player, print_game=True):
    if print_game:
        # выводим на экран игровое поле с номерами клеток
        game.print_board_numbers()

    letter = 'X'  # устанавливаем начальный символ 'X'
    while game.empty_squares():
        if letter == 'O':
            # если ход компьютера, выбираем случайный ход
            square = o_player.get_move(game)
        else:
            # если ход игрока, запрашиваем ввод
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                # выводим на экран сделанный ход и текущее игровое поле
                print('\n' + letter + ' сделал ход в клетку', square)
                game.print_board()
                print('')

            if game.current_winner:
                # если есть победитель, выводим сообщение и возвращаем его символ
                if print_game:
                    print(letter + ' победил!')
                return letter

            # переключаемся на ход другого игрока
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        # выводим сообщение о ничьей
        print('Ничья!')


# определяем игрока-человека
class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        # запрашиваем ввод игрока и проверяем его корректность
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + ', ваш ход. Введите номер клетки (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Некорректный ход. Попробуйте снова.')
        return val


# определяем игрока-компьютера, который делает случайные ходы
class RandomComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        # выбираем случайный ход
        square = random.choice(game.available_moves())
        return square


# запускаем игру, если этот файл запущен напрямую
if __name__ == '__main__':
    x_player = HumanPlayer('X')  # создаем игрока-человека со символом 'X'
    o_player = RandomComputerPlayer('O')  # создаем игрока-компьютера со символом 'O'
    t = TicTacToe()  # создаем объект игры
    play(t, x_player, o_player,
         print_game=True)  # запускаем игру с заданными игроками и выводом игрового поля после каждого хода
