#
# Укажите размер файла для скачивания: 123
# Какова скорость вашего соединения? 27
# Прошло 1 сек. Скачано 27 из 123 Мб (22%)
# Прошло 2 сек. Скачано 54 из 123 Мб (44%)
# Прошло 3 сек. Скачано 81 из 123 Мб (66%)
# Прошло 4 сек. Скачано 108 из 123 Мб (88%)
# Прошло 5 сек. Скачано 123 из 123 Мб (100%)

size = int(input('Укажите размер файла для скачивания: '))
speed = int(input('Какова скорость вашего соединения? '))

sec = 1

while sec * speed / size <= 1:
    print('Прошло {} сек. Скачано {} из {} Мб ({}%)'.format(sec, sec * speed, size, round(sec * speed / size * 100), 0))
    sec += 1
print('Прошло {} сек. Скачано {} из {} Мб ({}%)'.format(sec, size, size, round(size / size * 100), 0))

