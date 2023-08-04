# TODO здесь писать код
#
# import random
#
#
# class Karma:
#     def __init__(self, points):
#         self.points = points
#
#
# karma = 0
# def one_day():
#     a = karma
#     if random.randint(1, 10) == 10:
#         return random.choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
#     else:
#         a += random.randint(1, 7)
#     print(a)
#
# one_day()

import random

class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass

def get_karma():
    return random.randint(1, 7)

def one_day():
    karma = get_karma()

    if karma >= 500:
        raise StopIteration('Просветление достигнуто! Поздравляем!')

    try:
        if random.random() < 0.1:
            error = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
            raise error('Произошла ошибка')
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
        with open('karma.log', 'a', encoding='UTF-8') as log_file:
            log_file.write(f'Ошибка: {str(e)}\n')

def simulate_life():
    while True:
        try:
            one_day()
        except StopIteration as e:
            print(e)
            break

simulate_life()
