# TODO здесь писать код

my_str = input('Введите строку: ')
rev_str = my_str[::-1]
new_str = []

print(rev_str)

for i in range(len(rev_str)):
    if rev_str[i] != 'h':
        continue
    else:
        for j in range(i, len(rev_str)):
            new_str.append(rev_str[j])

print(new_str)
