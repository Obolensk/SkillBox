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
        self.hand=[]
        for i in range(2):
            self.hand.append(self.deck.pop(i))
        return self.hand

    def one_more(self):
        # print('\n - One more')
        self.hand.append(self.deck.pop(0))
        self.point_count()
        return self.hand

    def point_count(self):
        # print('\n - Point count')
        count = 0
        for i in self.hand:
            # print(i)
            if i[1] == 'J' or i[1] == 'Q' or i[1] == 'K':
                count += 10
            elif i[1] == 'A':
                if count > 10:
                    count += 1
                else:
                    count += 11
            else:
                count += i[1]
        # print('{} total count is {}'.format(self.name, count))
        return count

def winner(player, dealer):
    if player > 21:
        print('Перебор, ты проиграл!')
    elif dealer > 21:
        print('У Дилера перебор, ты выиграл!')
    elif player > dealer:
        print('Уррааа! Ты выиграл!')
    elif player == dealer:
        print('0:0!!!')
    else:
        print('Dealer win!')
    print('Результат дилера', dealer)
    print('Результат твой', player)


deck = Deck()
total = deck.make_deck()
# print(total)

me = Player('Me', total)
d = Player('Dealer', total)
# print('Cards in my Deck - ', len(total))
print('My hand', me.set_hand())
# me.set_hand()
# print('Cards in my Deck - ', len(total))
# print('Dealer hand', d.set_hand())
d.set_hand()
# print('Cards in my Deck - ', len(total))

while d.point_count() < 15:
    d.one_more()

while me.point_count() < 21:
    print(me.point_count())
    ans = input('Продолжаем? ')
    if ans == 'да':
        me.one_more()
    else:
        break

winner(me.point_count(), d.point_count())