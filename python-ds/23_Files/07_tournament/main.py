# TODO здесь писать код

import operator

file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/07_tournament/first_tour.txt', 'r')
old_file = file.read()
part_list = []
winners_list = []
print()

new_list = old_file.split('\n')
print(new_list)

for i in range(1, len(new_list)):
    # print(new_list[i])
    print()
    for a in new_list[i].split():
        # print(a)
        part_list.append(a)
    print(part_list)
    if part_list[2] > new_list[0]:
        winners_list.append(part_list)
    part_list = []

print(winners_list)
print()
print(winners_list.sort(key=operator.itemgetter(1, 2)))

news = sorted(operator.itemgetter(0, 1)(winners_list))
print(news)

print()
print()
print()
print()
print(winners_list)
print(sorted(winners_list))