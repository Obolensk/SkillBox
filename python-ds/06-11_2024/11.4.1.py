pers_num = int(input('Введите количество людей: '))
for hour in range(1, pers_num+1):
    print()
    print('Идет час', hour)
    for num in range(hour, pers_num):
        print('Номер в очереди', num)
print('Очередь обслужена!')
