import random

cards = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

class Card:

    def __init__(self, card, rank):
        self.card = card
        self.rank = rank

    def make_card(self):
        my_card = [self.card, self.rank]
        return my_card

class Deck:

    def make_deck(self):
        my_deck = []
        for i in range(1):
            for c in cards:
                for r in ranks:
                    i = Card(c, r)
                    my_deck.append(i.make_card())
        random.shuffle(my_deck)
        return my_deck

class Player:

    def __init__(self, deck):
        self.deck = deck

    def set_hand(self):
        hand = []
        for i in range(2):
            hand.append(self.deck.pop(i))
        print()
        return hand

    # def get_card(self):



d = Deck()
total = d.make_deck()
print(total)

me = Player(total)
dealer = Player(total)
print(len(total))
print(me.set_hand())
print(len(total))
# dealer.set_hand()
print(dealer.set_hand())
print(len(total))

if input('Ещё? ') == 'да':
    print(me.set_hand().append(total.pop(0)))

print()
print(me.set_hand())
print(len(total))


