# TODO здесь писать код

my_str = input('Введите строку: ')
decoded = []
new_str = []

for letter in my_str:
    new_str.append(letter)

print(new_str)

letter_count = 1
for i in range(len(new_str)-1):
    if new_str[i] == new_str[i+1]:
        letter_count += 1
        decoded.append(new_str[i] + str(letter_count))
        letter_count = 1
    else:
        decoded.append(new_str[i] + '1')

print(decoded)

