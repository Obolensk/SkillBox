# TODO здесь писать код

file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/07_tournament/first_tour.txt', 'r')
old_file = file.read()
part_list = []
winners_list = []

new_list = old_file.split('\n')

for i in range(1, len(new_list)):
    for a in new_list[i].split():
        part_list.append(a)
    if part_list[2] > new_list[0]:
        winners_list.append(part_list)
    part_list = []

res = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/07_tournament/second_tour.txt', 'w')
place = 1

for winners in sorted(winners_list):
    res.write('{}) {}. {} {} \n'.format(place, winners[1][0], winners[0], winners[2]))
    place += 1