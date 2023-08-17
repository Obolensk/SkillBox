
class Student:

    def __init__(self, name, group, estimates):
        self.name = name
        self.group = group
        self.estimates = estimates

    def success(self):
        avg = 0
        for i in self.estimates:
            avg += i
        avg /= len(self.estimates)
        return avg

    def info(self):
        print('Student {} from {}-th group have average ball {}'.format(self.name, self.group, self.success()))

    def dict_add(self, dct):
        dct[self.name] = self.success()


my_dict = {}
ivan = Student('Ivan', 1, [200, 3, 2, 3])
ivan.dict_add(my_dict)
dima = Student('Dima', 2, [18, 3, 2, 3])
dima.dict_add(my_dict)
stas = Student('Stas', 3, [4, 3, 4, 3])
stas.dict_add(my_dict)
gena = Student('Gena', 4, [5, 3, 4, 4])
gena.dict_add(my_dict)
toma = Student('Toma', 5, [5, 4, 5, 4])
toma.dict_add(my_dict)

sorted_dict = {}

for i in sorted(my_dict.values()):
    for k in my_dict:
        if my_dict[k] == i:
            sorted_dict[k] = i

print(sorted_dict)
print()

for i in sorted_dict:
    print('Средний балл студента {} составил {}!'.format(i, sorted_dict[i]))