first_class = []
second_class = []

for i in range(160, 177, 2):
    first_class.append(i)
print('Первый класс:', first_class)

for i in range(162, 181, 3):
    second_class.append(i)
print('Второй класс:', second_class)

first_class.extend(second_class)
print('Отсортированный список учеников:', sorted(first_class))