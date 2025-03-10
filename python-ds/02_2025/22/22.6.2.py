print('\n Task 1')

string = 'abcd'
tup = (10, 20, 30, 40)

print(zip(string, tup))

for item in zip(string, tup):
    print(item)

print('\n Task 2')


def my_zip(col_1, col_2):
    lst = [(col_1[i], col_2[i]) for i in range(min(len(col_1), len(col_2)))]
    return lst


f = ('а', 'б', 'в', 'г', 'д', 'е', 'ж')
s = '123456789'

print(my_zip(f, s))


