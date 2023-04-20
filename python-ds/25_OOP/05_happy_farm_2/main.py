# TODO здесь писать код

class Potato:
    # Класс, описывающий картошку
    def __init__(self, number):
        # Конструктор класса. Принимает номер картошки.
        self.number = number
        # Начальная стадия зрелости картошки равна 1.
        self.stage = 1

    def info(self):
        # Метод info возвращает строку с информацией о стадии зрелости и номере картошки.
        return f"Картошка номер {self.number}: стадия зрелости {self.stage}"

    def grow(self):
        # Метод grow увеличивает стадию зрелости картошки на 1, если она не достигнута максимальной (4).
        if self.stage < 4:
            self.stage += 1


class PotatoGarden:
    # Класс, описывающий грядку с картошкой.
    def __init__(self, size):
        # Конструктор класса. Принимает размер грядки.
        self.size = size
        self.potatoes = []
        # Создаем список картошек на грядке.
        for i in range(1, size + 1):
            self.potatoes.append(Potato(i))

    def info(self):
        # Метод info выводит информацию о грядке и всей картошке на ней.
        print(f"Грядка из {self.size} картошек.")
        for potato in self.potatoes:
            print(potato.info())

    def grow(self):
        # Метод grow увеличивает стадию зрелости всех картошек на грядке на 1.
        for potato in self.potatoes:
            potato.grow()

    def harvest(self):
        # Метод harvest собирает урожай, т.е. удаляет все картошки, у которых стадия зрелости равна 4, и возвращает список этих картошек.
        harvested_potatoes = []
        for potato in self.potatoes:
            if potato.stage == 4:
                harvested_potatoes.append(potato)
        self.potatoes = []
        return harvested_potatoes


class Gardener:
    # Класс, описывающий садовника.
    def __init__(self, name, garden):
        # Конструктор класса. Принимает имя садовника и грядку.
        self.name = name
        self.garden = garden

    def tend_garden(self):
        # Метод tend_garden заставляет садовника ухаживать за грядкой, вызывая метод grow у грядки и метод info для вывода информации о грядке и всей картошке на ней.
        print(f"{self.name} ухаживает за грядкой.")
        self.garden.grow()
        self.garden.info()

    def harvest_potatoes(self):
        # Метод harvest_potatoes заставляет садовника собрать урожай, вызывая метод harvest у грядки и выводит информацию о количестве собранных картошек и о каждой картошке.
        print(f"{self.name} собирает урожай.")
        harvested_potatoes = self.garden.harvest()
        print(f"{self.name} собрал {len(harvested_potatoes)} картошек.")
        for potato in harvested_potatoes:
            print(potato.info())


# Создаем грядку и экземпляр садовника.
garden = PotatoGarden(5)
gardener = Gardener('Иван', garden)

# Садовник ухаживает за грядкой и собирает урожай.
for i in range(4):
    gardener.tend_garden()
gardener.harvest_potatoes()
