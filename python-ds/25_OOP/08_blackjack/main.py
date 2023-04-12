# TODO здесь писать код

import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} {self.suit}'


class Deck:
    suits = ['Черви', 'Буби', 'Крести', 'Пики']
    ranks = ['Туз', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король']

    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 'Туз':
            self.aces += 1
        self.value += self.get_card_value(card)

    def get_card_value(self, card):
        if card.rank in ['Валет', 'Дама', 'Король']:
            return 10
        elif card.rank == 'Туз':
            return 11
        else:
            return int(card.rank)

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def add_card_to_hand(self, card):
        self.hand.add_card(card)

    def show_hand(self, dealer_start=True):
        print(f"\nРука игрока {self.name}")
        if dealer_start:
            print(" <карты скрыты>")
            print(f' {self.hand.cards[1]}')
        else:
            for card in self.hand.cards:
                print(f' {card}')
        print(f"Всего очков: {self.hand.value}")


class Dealer(Player):
    def show_hand(self, dealer_start=True):
        print(f"\nРука Дилера:")
        if dealer_start:
            print(" <карты скрыты>")
            print(f' {self.hand.cards[1]}')
        else:
            for card in self.hand.cards:
                print(f' {card}')
        print(f"Всего очков: {self.hand.value}")


deck = Deck()

player = Player("Player 1")
dealer = Dealer("Dealer")

player.add_card_to_hand(deck.deal())
dealer.add_card_to_hand(deck.deal())

player.add_card_to_hand(deck.deal())
dealer.add_card_to_hand(deck.deal())

player.show_hand()
dealer.show_hand()

game_over = False

while not game_over:
    choice = input("\nWould you like to hit or stay? ")
    if choice.lower() == 'hit':
        player.add_card_to_hand(deck.deal())
        player.show_hand()
        dealer.show_hand()
        if player.hand.value > 21:
            print("\nYou busted!")
            game_over = True
    else:
        while dealer.hand.value < 17:
            dealer.add_card_to_hand(deck.deal())
        player.show_hand()
        dealer.show_hand(False)
        if dealer.hand.value > 21:
            print("\nДилер проиграл, ты выиграл!")
            game_over = True
        elif dealer.hand.value > player.hand.value:
            print("\nДилер выиграл!")
            game_over = True
        elif dealer.hand.value < player.hand.value:
            print("\nТы выиграл!")
            game_over = True


