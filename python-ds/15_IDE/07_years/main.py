# TODO здесь писать код

def three_nums(a):
    i = 0
    three_nums_year = a
    a_1 = a % 10
    a //= 10
    a_2 = a % 10
    if a_2 == a_1:
        i += 1
    a //= 10
    a_3 = a % 10
    if a_3 == a_2:
        i += 1
    if a_3 == a_1:
        i += 1
    a //= 10
    a_4 = a % 10
    if a_4 == a_3:
        i += 1
    if a_4 == a_2:
        i += 1
    if a_4 == a_1:
        i += 1
    if i == 3:
        print(three_nums_year)

# three_nums(1555)

first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))

print('Года от', first_year, 'до', second_year, 'с тремя одинаковыми цифрами:')

for i in range (first_year+1, second_year):
    three_nums(i)
