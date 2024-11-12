string = input('Введите строку: ')
# string = 'abbc'
# sym_num = 3
sym_num = int(input('Номер символа: '))
count = 0
new_string = []

for i in range(len(string)):
    if i == sym_num-1:
        new_string.append(string[i-1])
        new_string.append(string[i+1])
        print('Символ слева:', new_string[0])
        print('Символ справа:', new_string[1])

print(new_string)

for i in new_string:
    if i == string[sym_num-1]:
        count += 1
if count == 1:
    print('Есть ровно один такой же символ.')
elif count == 2:
    print('Оба соседа совпадают')
else:
    print('Таких же символов нет.')



# print(''.join(new_string))
