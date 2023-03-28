# TODO здесь писать код

import random
class Card:
    def __init__(self,
                 rank= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз'],
                 suit= ['пики', 'крести', 'буби', 'черви', 'туз']):
        self.rank = rank
        self.suit = suit
    def make(self):
        cards = []
        deck = []
        while True:
            cards.append(self.rank[random.randint(0, len(my_card.rank) - 1)])
            cards.append(self.suit[random.randint(0, len(my_card.suit) - 1)])
            if cards not in deck:
                deck.append(cards)
                cards = []
            else:
                cards = []
                continue
            return deck
class Deck:
    def __init__(self, new_card):
        self.new_card = new_card
    # def make(self):
    #     cards = []
    #     deck = []
    #     cards.append(random.randint(0, len(my_card.suit)-1))
    #     cards.append(random.randint(0, len(my_card.rank)-1))
    #     deck.append(cards)
    #     cards = []

my_card = Card()
print(len(my_card.suit))
print(len(my_card.rank))

print(my_card.make())

# while True:
#     print(my_card.make())