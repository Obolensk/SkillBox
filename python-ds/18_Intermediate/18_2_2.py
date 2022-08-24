
my_str = input('Введите строку: ')
sym = input('Введите дополнительный символ: ')

double_list = [i + i for i in my_str]

add_sym = [i + sym for i in double_list]

print('Список удвоенных символов:', double_list)
print('Склейка с дополнительным символом:', add_sym)