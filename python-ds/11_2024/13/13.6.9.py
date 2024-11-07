
def rock_paper_scissors():
    # Здесь будет игра "Камень, ножницы, бумага"
    comp_step = 'rock'
    user_step = int(input('Введите свой ход. 1 - Камень, 2 - Ножницы, 3 - Бумага: '))
    if user_step == 1:
        print('Попробуйте еще раз!\n')
        rock_paper_scissors()
    elif user_step == 2:
        print('Вы проиграли!\n')
        mainMenu()
    elif user_step == 3:
        print('Победа\n')
        mainMenu()



def guess_the_number():
    user_step = int(input('Угадай загаданное число? '))
    if user_step == 8:
        print('Победа!!!\n')
    else:
        guess_the_number()
        mainMenu()
    # Здесь будет игра "Угадай число"


def mainMenu():
    game = int(input('Выберите игру. 1 - Камень, ножницы, бумага. 2 - Угадай число: '))
    if game == 1:
        rock_paper_scissors()
    elif game == 2:
        guess_the_number()
    # Здесь главное меню игры


mainMenu()
