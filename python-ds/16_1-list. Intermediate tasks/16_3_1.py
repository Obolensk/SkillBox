
S = input('Введите строку: ')
S_list = []
count = 0
for sym in S:
    S_list.append(sym)
for i in range(len(S_list)):
    if S_list[i] == ':':
        S_list[i] = ';'
    print(S_list[i], end='')