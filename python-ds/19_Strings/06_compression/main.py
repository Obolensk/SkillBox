# TODO здесь писать код

my_str = input('Введите строку: ')
decoded = []
new_str = []

for letter in my_str:
    new_str.append(letter)

# print(new_str)

letter_count = 1
for i in range(len(new_str)):
    if i == 0:
        decoded.append(new_str[0])
    elif new_str[i] == new_str[i - 1]:
        letter_count += 1
        if i == len(new_str) - 1:
            decoded.append(str(letter_count))
    else:
        decoded.append(str(str(letter_count)))
        decoded.append(new_str[i])
        letter_count = 1
        if i == len(new_str) - 1:
            decoded.append(str(letter_count))

print(''.join(decoded))
