# TODO здесь писать код
class Student:
    def __init__(self, name, group, marks):
        self.name = name
        self.group = group
        self.marks = marks
    def edu(self):
        sum = 0
        for i in self.marks:
            sum += i
        total = sum / len(self.marks)
        self.marks.append(total)
        return total
    def print_students(self):
        print()
        print('Фамилия студента: {}'.format(self.name))
        print('Номер группы: {}'.format(self.group))
        print('Успеваемость студента: {}'.format(self.marks))
    def add_in_dict(self, my_dict):
        self.my_dict = my_dict
        self.my_dict[self.name] = self.marks[5]

ivanov = Student('Ivanov', 123, [1, 2, 33, 4, 5])
petrov = Student('Petrov', 234, [12, 2, 3, 4, 5])
stepanov = Student('Stepanov', 345, [7, 2, 3, 4, 5])
sergeev = Student('Sergeev', 456, [0, 1, 2, 3, 4])
panov = Student('Panov', 567, [1, 2, 3, 4, 5])

ivanov.edu()
petrov.edu()
stepanov.edu()
sergeev.edu()
panov.edu()

all_students = dict()
ivanov.add_in_dict(all_students)
petrov.add_in_dict(all_students)
stepanov.add_in_dict(all_students)
sergeev.add_in_dict(all_students)
panov.add_in_dict(all_students)

sort_students = dict(sorted(all_students.items(), key=lambda item: item[1]))
print('Отсортированный список студентов: ')
for key in sort_students:
    print(key, sort_students[key])