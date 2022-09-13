
my_str = input('Введите строку: ')

# print(my_str.islower())

hi = 0
low = 0

for letter in my_str:
    if letter.islower():
        low += 1
    else:
        hi += 1

# print('hi = ', hi, 'low = ', low)

if hi > low:
    print(my_str.upper())
else:
    print(my_str.lower())