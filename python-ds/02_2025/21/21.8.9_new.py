
my_dict = dict()

n = int(input('Сколько записей вносится в протокол? '))

for i in range(n):
    print(i+1, end=' ')
    game = input('Запись: ')
    print(game.split())
    name = game.split()[1]
    score = int(game.split()[0])
    if name in my_dict:
        my_dict[name + '_' + str(i)] = score
    else:
        my_dict[name] = score
print(my_dict)
print(sorted(my_dict))
print(sorted(my_dict.values()))

for na, sc in my_dict.items():

# new_dict = dict()
# part_list = list()
# score_list = list()
# for na, sc in my_dict.items():
#     print(na, sc)
#     part_list.append(na)
#     score_list.append(sc)

# print(part_list)
# print(score_list)
#
# for i in part_list:
#     count = 0
#     if max(part_list) == i:
#         count += 1
#     if count != 1:
#






# print(my_dict)
# print(sorted(my_dict))
# print(sorted(my_dict.values()))
first = sorted(my_dict.values())[-1]
second = sorted(my_dict.values())[-2]
third = sorted(my_dict.values())[-3]

# print(my_dict)
# print('d' in my_dict)
print()

print('first = ', first)
print('second = ', second)
print('third = ', third)
