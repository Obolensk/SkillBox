a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
# print(a)
fives = 0
three = 0
for i in a:
    if i == 5:
        fives += 1

print('Кол-во цифр 5 при первом объединении: ', fives)

for i in range(fives):
    a.remove(5)
# print(a)

a.extend(c)
# print(a)

for i in a:
    if i == 3:
        three += 1
print('Кол-во цифр 3 при втором объединении: ', three)
print('Итоговый список: ', a)

# TODO переписать программу
