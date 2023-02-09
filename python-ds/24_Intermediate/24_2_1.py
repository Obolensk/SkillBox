

try:
    BRUCE_WILLIS = 42
    input_data = input('Введите строку: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError:
    print('Я не могу преобразовать строку {} в число'.format(input_data))
except IndexError:
    print('В строке {} меньше пяти элементов, а мне нужен именно пятый!'.format(input_data))
except:
    print('Вроде ошибка какая-то?!?!')