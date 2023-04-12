# TODO здесь писать код
import random
class Deck:
    def __init__(self,
                 rank= [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз'],
                 suit= ['пики', 'крести', 'буби', 'черви']):
        self.rank = rank
        self.suit = suit
    def make(self):
        cards = []
        deck = []
        fault = 0
        while fault < 100:
            cards.append(self.rank[random.randint(0, len(self.rank) - 1)])
            cards.append(self.suit[random.randint(0, len(self.suit) - 1)])
            if cards not in deck:
                deck.append(cards)
                cards = []
                fault = 0
            else:
                cards = []
                fault += 1
                continue
        # print('len(deck) = ', len(deck))
        # print()
        return deck
class Player:
    def __init__(self, name, score=0, hand_score=0):
        self.name = name
        self.score = score
        self.hand_score = hand_score
    def first_deal(self, deck):
        my_hand = []
        deck = Deck()
        my_hand.append(deck.make()[0])
        my_hand.append(deck.make()[1])
        if my_hand[0][0] in range(2, 10):
            self.hand_score += my_hand[0][0]
        else:
            self.hand_score += 10
        if my_hand[1][0] in range(2, 10):
            self.hand_score += my_hand[1][0]
        else:
            self.hand_score += 10
        self.score += self.hand_score
        # print('Рука игрока {} равна {} очков!'.format(self.name, score))
        if self.score < 22:
            print('Игрок {} У Вас {} очков'.format(self.name, self.score))
            ans = input('Ещё? ')
            if ans == 'да':
                self.first_deal(deck)
        else:
            print('Перебор, Вы проиграли!')
            # break
        return my_hand, self.score

deck = Deck()

my_deck = deck.make()
print()
print(my_deck)

print()
print('Создаю игроков')
me = Player('I am')
dealer = Player('Дилер')
print('Моя рука {}'.format(me.first_deal(my_deck)))
print()
print('Рука дилера {}'.format(dealer.first_deal(my_deck)))
