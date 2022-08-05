# TODO здесь писать код

word = input('Введите слово: ')
new_list = []

for sym in word:
    new_list.append(sym)
print('new_list - ', new_list)
print('word - ', word)

count = 0
for i in new_list:
    int_list = new_list.remove(i)
    if i in int_list:
        count += 1
        print(i)

#
# for i in range(len(new_list)):
#     if new_list[i] in word:
#         count += 1
