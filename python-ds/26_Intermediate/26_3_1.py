
class Ship:

    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return '\nМодель корабля: {model}'.format(
            model=self.__model
        )

    def sail(self):
        print('\nКорабль плывет!')


class WarShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print('\nКорабль атакует с помощью оружия', self.gun)

class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.tonnage_load = 0

    def load(self):
        print('\nЗагружаем корабль!')
        self.tonnage_load += 1
        print('\nТекущая загруженность равна:', self.tonnage_load)

    def unload(self):
        print('\nРазгружаем корабль')
        if self.tonnage_load > 0:
            self.tonnage_load -= 1
        else:
            print('Корабль уже разгружен!')
        print('Текущая загруженность равна:', self.tonnage_load)



warship = WarShip('Petr I', 'MyGuns')
warship.sail()
warship.attack()
print(warship)
print()
cargo = CargoShip('IVAN_1')
cargo.load()
cargo.load()
print(cargo)
cargo.unload()

