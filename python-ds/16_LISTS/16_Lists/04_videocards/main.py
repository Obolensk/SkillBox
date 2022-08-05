# TODO здесь писать код

all_list = []
vc_nums = int(input('Количество видеокарт: '))
for i in range(vc_nums):
    print(i+1, end=' ')
    vc_index = int(input('Видеокарта: '))
    all_list.append(vc_index)

print('Старый список видеокарт:', all_list)
max = max(all_list)
all_list.remove(max)

for vc in all_list:
    if vc == max:
        all_list.remove(vc)
print('Новый список видеокарт: ', all_list)





