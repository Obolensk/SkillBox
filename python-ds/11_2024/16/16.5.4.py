total = []
card_num = int(input('Количество видеокарт: '))

for i in range(1, card_num + 1):
    print(i, end=' ')
    card = int(input('Видеокарта: '))
    total.append(card)

new_list = list(total)

for i in total:
    if i == max(total):
        new_list.remove(i)

print('Старый список видеокарт:', total)
print('Новый список видеокарт:', new_list)