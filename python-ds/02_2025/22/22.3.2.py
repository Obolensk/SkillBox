from Lib.test.test_pyrepl.support import multiline_input

data_input = {"a": 10, "b": 20}
tp = type(data_input)
if isinstance(data_input, str):
    desc = '(строка)'
    mute = 'Неизменяемый (immutable)'
if isinstance(data_input, list):
    desc = '(список)'
    mute = 'Изменяемый (mutable)'
if isinstance(data_input, int):
    desc = '(целое число)'
    mute = 'Неизменяемый (immutable)'
if isinstance(data_input,float):
    desc = '(вещественное число)'
    mute = 'Неизменяемый (immutable)'
if isinstance(data_input, dict):
    desc = '(словарь)'
    mute = 'Изменяемый (mutable)'
if isinstance(data_input, tuple):
    desc = '(кортеж)'
    mute = 'Неизменяемый (immutable)'


print('data_input = "{}"'.format(data_input))
print('Тип данных: {} {}'.format(type(data_input), desc))
print(mute)
print('id объекта: ', id(data_input))

