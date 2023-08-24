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

    def __init__(self, name, deck, hand=[]):
        self.name = name
        self.deck = deck
        self.hand = hand

    def set_hand(self):
        for i in range(2):
            self.hand.append(self.deck.pop(i))
        print()
        return self.hand

    def one_more(self):
        self.hand.append(self.deck.pop(0))
        return self.hand

class Dealer:

    def __init__(self, name, deck, dealer_hand=[]):
        self.name = name
        self.deck = deck
        self.dealer_hand = dealer_hand

    def set_hand(self):
        for i in range(2):
            self.dealer_hand.append(self.deck.pop(i))
        print()
        return self.dealer_hand

    def one_more(self):
        self.dealer_hand.append(self.deck.pop(0))
        self.point_count()
        return self.dealer_hand

    def point_count(self):
        count = 0
        for i in self.dealer_hand:
            print(i)
            if i[1] == 'J' or i[1] == 'Q' or i[1] == 'K':
                count += 10
            elif i[1] == 'A':
                if count > 10:
                    count += 1
                else:
                    count += 11
            else:
                count += i[1]
        print('{} total count is {}'.format(self.name, count))
        return count



d = Deck()
total = d.make_deck()
print(total)

me = Player('Me', total)
d = Dealer('Dealer', total)
print('Cards in my Deck - ', len(total))
print('My hand', me.set_hand())
print('Cards in my Deck - ', len(total))
# dealer.set_hand()
print('Dealer hand', d.set_hand())
print('Cards in my Deck - ', len(total))

# if input('Ещё? ') == 'да':
#     print(me.one_more())

d.point_count()
d.one_more()


# print()
# print(me.set_hand())
# print(len(total))


