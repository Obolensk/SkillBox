# TODO здесь писать код

rol_nums = int(input('Кол-во коньков: '))
rol_sizes = []
feet_sizes = []
total = 0

for i in range(rol_nums):
    print('Размер', i+1, end='')
    rol_size = int(input('-й пары: '))
    rol_sizes.append(rol_size)
print('rol_sizes = ', rol_sizes)

hum_nums = int(input('Кол-во людей: '))
for i in range(hum_nums):
    print('Размер ноги ', i+1, end='')
    foot_size = int(input('-го человека: '))
    feet_sizes.append(foot_size)
print('feet_sizes = ', feet_sizes)

x = rol_nums
for foot in feet_sizes:
    for i in range(x):
        if foot <= rol_sizes[i]:
            rol_sizes.remove(rol_sizes[i])
            total += 1
            x -= 2

print()
print('Наибольшее кол-во людей, которые могут взять ролики: ', total)






