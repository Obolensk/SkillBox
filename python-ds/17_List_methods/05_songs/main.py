violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код
new_list = []
for i in range(len(violator_songs)):
    new_list.append(violator_songs[i][0])
print(new_list)

time = 0
song_num = int(input('Сколько песен выбрать? '))
for i in range(song_num):
    print('Название ', i+1, end='')
    song_name = input('-й песни: ')
    time += violator_songs[new_list.index(song_name)][1]
print('Общее время звучания песен:', round(time, 2), 'минуты')
