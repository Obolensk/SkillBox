
cont_num = int(input('Количество контейнеров: '))
boxes = []
ind = 0
new = 0
for _ in range(cont_num):
    cont = int(input('Введите вес контейнера: '))
    boxes.append(cont)


print(boxes)
print(sorted(boxes))

def get_new():
    new = int(input('Введите вес нового контейнера: '))
    if new > 200:
        get_new()
    else:
        boxes.append(new)
        # print(sorted(boxes))
        new_boxes = sorted(boxes)
        new_boxes.reverse()
        # print(new_boxes)
    return new_boxes.index(new)

print('Номер, который получит новый контейнер:', get_new() + 1)