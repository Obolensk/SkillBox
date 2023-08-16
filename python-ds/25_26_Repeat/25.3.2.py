
class Family:
    def __init__(self, name, money, house):
     self.name = name
     self.money = money
     self.house = house

    def info(self):
        print('\nName: {}\nMoney: {}\nHouse: {}\n'.format(self.name, self.money, self.house))

    def earn(self, summ=10**1):
        print("\nTry to earn money + {}".format(summ))
        self.summ = summ
        self.money += summ
        print('Money is {}'.format(self.money))

    def buy_house(self, price=10**2):
        self.price = price
        print('Try to buy a house for: {}'.format(self.price))
        if self.price > self.money:
            print('Money is not enough!')
            self.earn()
            self.buy_house()
        else:
            self.money -= self.price
            self.house = True
            print('House purchased!')
            self.info()

f1 = Family('Ivanovy', 10**1, False)
f1.info()

f1.buy_house()
