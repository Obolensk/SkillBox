S = input('Введите строку: ')
sym_num = int(input('Номер символа: '))
S_list = []
for sym in S:
    S_list.append(sym)
print('Символ слева:', S_list[sym_num-2])
print('Символ справа:', S_list[sym_num])
if S_list[sym_num-1] == S_list[sym_num] == S_list[sym_num-2]:
    print('Есть два таких же')
elif S_list[sym_num-1] == S_list[sym_num] or S_list[sym_num-1] == S_list[sym_num-2]:
    print('Есть ровно один такой же символ')
else:
    print('Таких же символов нет.')

