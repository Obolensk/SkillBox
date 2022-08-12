# N = int(input('Кол-во человек: '))
# K = int(input('Какое число в считалке? '))
N = 5
K = 7

print('Значит, выбывает каждый ', K,'-й человек')

list = []
if N == len(list):
    a = 0
else:
    a = K % N


for i in range(N):
    list.append(i+1)
# print('Текущий круг людей: ', list)
# print('Начало счёта с номера', list[a])

while len(list) > 1:
    print('Текущий круг людей: ', list)
    print('a', a)
    print('Начало счёта с номера', list[a-2])
    print('Выбывает человек под номером ', list[a-1])
    print()
    list.pop(a-1)

print(list)
print()
print('Остался человек под номером', list[0])
