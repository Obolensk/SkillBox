song_nums = 3
songs = ['Halo', 'Enjoy the Silence', 'Clean']
total = 0


violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


print(violator_songs['Clean'])
# print()

for song in songs:
    for item in violator_songs:
        if item == song:
            total += violator_songs[song]

print(round(total, 2))
