# TODO здесь писать код

# Задача 9

# Алгоритм такой:
# 1. При вводе списка, добавляем оба элемента в словарь как ключи, а значения по умолчанию у первого элемента - ноль, а у нулевого - значение первого элемента + 1.

pers_nums = int(input('Введите количество человек: '))
pers_dict = dict()

for i in range(pers_nums - 1):
  print(i + 1, end=' ')
  pair = input('пара: ').split()
  # print(pair)
  if pair[1] in pers_dict:
    pers_dict[pair[0]] = pers_dict[pair[1]] + 1
  else:
    pers_dict[pair[1]] = 0
    pers_dict[pair[0]] = pers_dict[pair[1]] + 1
  # print()
  # print(pers_dict)
# print()
# print(sorted(pers_dict.items()))

print()
print('“Высота” каждого члена семьи:')
for pers in sorted(pers_dict.items()):
  for i in pers:
    print(i, end=' ')
  print()

