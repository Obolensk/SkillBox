# TODO здесь писать код

class Property:
    def __init__(self, worth):
        self.worth = worth

    def calculate_tax(self):
        pass

class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 1000

class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 200

class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 500

def main():
    money = int(input("Введите количество ваших денег: "))
    apartment_worth = int(input("Введите стоимость квартиры: "))
    car_worth = int(input("Введите стоимость машины: "))
    country_house_worth = int(input("Введите стоимость дачи: "))

    total_tax = 0

    apartment = Apartment(apartment_worth)
    car = Car(car_worth)
    country_house = CountryHouse(country_house_worth)

    total_tax += apartment.calculate_tax()
    total_tax += car.calculate_tax()
    total_tax += country_house.calculate_tax()

    if money < total_tax:
        print("Не хватает денег на оплату налога.")
        print("Необходимая сумма:", total_tax)
        print("Ваша сумма:", money)
    else:
        print("Налог на соответствующее имущество:", total_tax)
        print("Денег достаточно.")

main()