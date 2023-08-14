# TODO здесь писать код

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
        with open('karma.log', 'a', encoding='utf-8') as log_file:
            log_file.write(f'Ошибка: {str(e)}\n')


def simulate_life():
    karma = 0
    while karma < 500:
        try:
            one_day()
            karma += get_karma()
        except StopIteration as e:
            print(e)
            return

        print(f'Текущая карма: {karma}')


simulate_life()
