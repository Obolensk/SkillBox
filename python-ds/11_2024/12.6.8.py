import math

hours = float(input('На сколько градусов повернулась часовая стрелка? '))

minutes = (hours * 12) % 360

print('Минутная стрелка повернулась на', minutes, 'градусов с начала последнего часа!')