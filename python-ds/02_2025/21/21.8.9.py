
my_dict = dict()

n = int(input('Сколько записей вносится в протокол? '))

for i in range(n):
    print(i+1, end=' ')
    game = input('Запись: ')
    print(game.split())
    name = game.split()[1]
    score = int(game.split()[0])
    my_dict[score] = name

print(my_dict)
print(sorted(my_dict))
first = sorted(my_dict)[-1]
second = sorted(my_dict)[-2]
third = sorted(my_dict)[-3]
print(my_dict.values())
print('d' in my_dict.values())
print()

print('first = ', my_dict[first], first)
print('second = ', my_dict[second], second)
print('third = ', my_dict[third], third)
