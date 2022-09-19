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
        if new_str[i] == new_str[i-1]:
            decoded.pop(i-1)
    else:
        letter_count = 1
        decoded.append(new_str[i] + str(letter_count))

print(decoded)

# Надо прописать подробный алгоритм
# 1. Делаю список
# 2. Считаю количество элементов подряд (вот это надо подробнее расписать)
# ...
# 3. Вывожу элемент + количество
# 4.
# 5.
# 6.
# 7.
