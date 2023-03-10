# TODO здесь писать код


def amount(num):
    res = 0
    my_list = []
    for i in num.split():
        my_list.append(i)
    print(my_list)
    if my_list[1] == '+':
        res = int(my_list[0]) + int(my_list[2])
    elif my_list[1] == '-':
        res = int(my_list[0]) - int(my_list[2])
    elif my_list[1] == '*':
        res = int(my_list[0]) * int(my_list[2])
    elif my_list[1] == '/':
        res = int(my_list[0]) / int(my_list[2])
    elif my_list[1] == '%':
        res = int(my_list[0]) % int(my_list[2])
    elif my_list[1] == '//':
        res = int(my_list[0]) // int(my_list[2])
    else:
        print('Обнаружена ошибка в строке: {}'.format(num))
        ans = input('Хотите исправить? ')
        if ans == 'да' or ans == 'Да':
            new_num = input('Введите исправленную строку: ')
            res += amount(new_num)
    return res

total = 0
with open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/24_Exceptions/05_text_calc/calc.txt', 'r') as calc:
    for i in calc:
        total += amount(i)
        print()

print('Сумма результатов:', total)