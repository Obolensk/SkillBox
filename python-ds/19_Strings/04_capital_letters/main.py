# TODO здесь писать код

my_str = input('Введите строку: ').split()

new_str = []

for word in my_str:
    new_str.append(word.capitalize())
print(' '.join(new_str))
