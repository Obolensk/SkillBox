class Family():
    surname = 'common surname'
    money = 100
    have_a_house = False

    def info(self):
        print()
        print('Our surname is {} \nOur capital is {} \nOwn a house is {}'.format(
            self.surname, self.money, self.have_a_house)
        )

    def earn_money(self, amount):
        self.money += amount
        print()
        print('Earned money is {} \nNow total summ is {}'.format(
            amount, self.money)
        )

    def buy_house(self, house_price, discount=0):
        print()
        if house_price * (100 - discount) / 100 <= self.money:
            self.money -= house_price * (100 - discount) / 100
            self.have_a_house = True
            print('Congrats!!! New house was purchased!!!')
        else:
            print('Not enough money!')


smith = Family()
smith.surname = 'Smith'
smith.money = 150

smith.info()

smith.earn_money(10)
smith.info()
print()
print('Try to buy a new house!')


while smith.have_a_house == False:
    smith.earn_money(30)
    smith.buy_house(200, 10)
else:
    print("Wow, It's done!!!")
    print('The money after house buying is {}'.format(smith.money))
