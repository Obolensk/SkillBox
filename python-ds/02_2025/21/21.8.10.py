print('\n Task 1')

string = 'abcd'
tup = (10, 20, 30, 40)

print(zip(string, tup))

for item in zip(string, tup):
    print(item)

print('\n Task 2')


def my_zip(col_1, col_2):
    # col_1 = 'abcdefg'
    # col_2 = (10, 20, 30, 40, 50, 60, 70)
    print(len(col_1))
    print(len(col_2))
    for i in range(min(len(col_1), len(col_2))):
        lst = []
        lst.append(col_1[i])
        lst.append(col_2[i])
        print(tuple(lst))

f = ('а', 'б', 'в', 'г', 'д', 'е', 'ж')
# f = {
#     'а': 11,
#     'б': 22,
#     'в': 33,
#     'г': 44,
#     'д': 55,
#     'е': 66,
#     'ж': 77}
s = '123456789'

my_zip(f, s)


