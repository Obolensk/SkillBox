# TODO здесь писать код

initial_list = [1, 4, -3, 0, 10]
shift = int(input('Сдвиг: '))
new_list = []

for i in range(len(initial_list)):
    new_list.append(initial_list[i - shift])
print(new_list)

