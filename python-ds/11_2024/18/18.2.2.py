
string = input('Введите строку: ')
sym = input('Введите дополнительный символ: ')

new_string = [i + i for i in string]

print('Список удвоенных символов:', new_string)

add_sym = [i + sym for i in new_string]

print('Склейка с дополнительным символом:', add_sym)