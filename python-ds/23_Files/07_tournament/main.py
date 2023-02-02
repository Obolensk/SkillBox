# TODO здесь писать код
import os

file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/07_tournament/first_tour.txt', 'r')
old_file = file.read()
part_list = []
winners_list = []
print()

new_list = old_file.split('\n')
print(new_list)

for i in range(1, len(new_list)):
    print()
    for a in new_list[i].split():
        part_list.append(a)
    print(part_list)
    if part_list[2] > new_list[0]:
        winners_list.append(part_list)
    part_list = []

print()
print(winners_list)
print(sorted(winners_list))
print()
text = []
text.append(len(winners_list))
# print(len(winners_list))
place = 1
for winners in sorted(winners_list):
    print('{}) {}. {} {}'.format(place, winners[1][0], winners[0], winners[2]))
    place += 1

print()
print()

res = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/07_tournament/second_tour.txt', 'a')
result = res.write(text)