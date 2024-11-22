a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
t = 0
for i in a:
    if i == 5:
        t += 1
        a.remove(i)
print('Кол-во цифр 5 при первом объединении:', t)

a.extend(c)
t = 0
for i in a:
    if i == 3:
        t += 1

print('Кол-во цифр 3 при втором объединении:', t)
print('Итоговый список:', a)