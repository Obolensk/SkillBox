# TODO здесь писать код

container_nums = int(input('Количество контейнеров: '))
cont_list = []
for i in range(container_nums):
    weight = int(input('Введите вес контейнера: '))
    cont_list.append(weight)

new_weight = int(input('Введите вес нового контейнера: '))
new_position = 1
for i in range(container_nums):
    if new_weight <= cont_list[i]:
        new_position += 1
    else:
        break
print('Номер, который получит новый контейнер:', new_position)


