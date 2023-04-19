# TODO здесь писать код

import random

class Card: # Класс Card описывает карту в колоде.
    def __init__(self, suit, rank): # Каждая карта имеет свою масть и ранг.
        self.suit = suit
        self.rank = rank

    def __str__(self): # метод для вывода карты в виде строки
        return f'{self.rank} {self.suit}'

class Deck: # Класс Deck создаёт и перемешивает колоду, а также выдаёт по одной карте
    suits = ['Черви', 'Буби', 'Крести', 'Пики']
    ranks = ['Туз', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король']

    def __init__(self): # конструктор
        self.cards = [] # список карт
        for suit in self.suits: # создаем колоду из 52 карт (4 масти по 13 карт в каждой)
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))
        self.shuffle() # перемешиваем колоду

    def shuffle(self): # метод для перемешивания колоды
        random.shuffle(self.cards)

    def deal(self): # метод для выдачи одной карты из колоды
        return self.cards.pop()

class Hand: # Класс Hand представляет карты в руке игрока (или дилера), хранит их и вычисляет их значение
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    # методы для работы с картами в руке
    def add_card(self, card): # добавляем карту в руку
        self.cards.append(card)
        if card.rank == 'Туз': # определяем значение карты и общее значение очков в руке
            self.aces += 1
        self.value += self.get_card_value(card)

    def get_card_value(self, card): # определяем значение карты исходя из ее ранга
        if card.rank in ['Валет', 'Дама', 'Король']:
            return 10
        elif card.rank == 'Туз':
            return 11
        else:
            return int(card.rank)

    def adjust_for_ace(self): # корректируем общее значение очков при наличии тузов
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Player: # Класс Player представляет игрока с заданным именем и рукой карт
    def __init__(self, name):
        self.name = name
        self.hand = Hand() # создаем объект класса Hand

    def add_card_to_hand(self, card): # добавляем карту в руку игрока
        self.hand.add_card(card)

    def show_hand(self, dealer_start=True): # выводим на экран карты в руке игрока
        print(f"\nРука игрока {self.name}")
        if dealer_start:
            print(" <карты скрыты>")
            print(f' {self.hand.cards[1]}')
        else:
            for card in self.hand.cards:
                print(f' {card}')
        print(f"Всего очков: {self.hand.value}")

class Dealer(Player): # Класс Dealer наследуется от класса Player и добавляет функционал по выводу руки дилера с одной скрытой картой в начале игры
    def show_hand(self, dealer_start=True): #
        print(f"\nРука Дилера:")
        if dealer_start:
            print(" <карты скрыты>")
            print(f' {self.hand.cards[1]}')
        else:
            for card in self.hand.cards:
                print(f' {card}')
        print(f"Всего очков: {self.hand.value}")

deck = Deck() # Создаем объект колоды

player = Player("Игрок 1") # Создаем объект игрока
dealer = Dealer("Дилер") # Создаем объект дилера


# Выдаем по две карты каждому

player.add_card_to_hand(deck.deal())
dealer.add_card_to_hand(deck.deal())

player.add_card_to_hand(deck.deal())
dealer.add_card_to_hand(deck.deal())

player.show_hand() # Игрок показывает карты
dealer.show_hand() # Дилер показывает карты

game_over = False # Переменная game_over устанавливается в True, если игра закончена.

while not game_over: # В цикле игрок может запросить еще карты до тех пор, пока не примет решение пасовать.
    choice = input("\nЕщё или пас? ") #
    if choice.lower() != 'пас':
        player.add_card_to_hand(deck.deal())
        player.show_hand()
        dealer.show_hand()
        if player.hand.value > 21: # если сумма очков превысила 21, игрок проиграл
            print("\nПеребор! Ты проиграл!")
            game_over = True
    else:
        while dealer.hand.value < 17: # дилер берет карты, пока его сумма очков меньше 17
            dealer.add_card_to_hand(deck.deal())
        player.show_hand()
        dealer.show_hand(False)
        if dealer.hand.value > 21: # если сумма очков дилера превысила 21, игрок выиграл
            print("\nДилер проиграл, ты выиграл!")
            game_over = True
        elif dealer.hand.value > player.hand.value: # если сумма очков дилера больше суммы очков игрока, игрок проиграл
            print("\nДилер выиграл!")
            game_over = True
        elif dealer.hand.value < player.hand.value: # если сумма очков игрока больше суммы очков дилера, игрок выиграл
            print("\nТы выиграл!")
            game_over = True


