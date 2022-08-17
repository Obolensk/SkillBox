# TODO здесь писать код

rol_nums = int(input('Кол-во коньков: '))
rol_sizes = ["""41, 40, 39, 42"""]
feet_sizes = ["""42, 41, 42"""]
total = 0

for i in range(rol_nums):
    print('Размер', i+1, end='')
    rol_size = int(input('-й пары: '))
    rol_sizes.append(rol_size)

hum_nums = int(input('Кол-во людей: '))
for i in range(hum_nums):
    print('Размер ноги ', i+1, end='')
    foot_size = int(input('-го человека: '))
    feet_sizes.append(foot_size)

# print('rol_sizes', rol_sizes)
# print('feet_sizes', feet_sizes)
# print('len(rol_sizes)', len(rol_sizes))


x = len(rol_sizes)
for foot in feet_sizes:
    # print('foot',foot)
    for i in range(x):
        # print()
        print('foot', type(foot))
        print('rol_sizes[i]', type(rol_sizes[i]))
        if foot <= rol_sizes[i]:
            rol_sizes.remove(rol_sizes[i])
            total += 1
            x -= 2
        # print('total', total)

print('Наибольшее кол-во людей, которые могут взять ролики: ', total)






