

# ip = input('Введите IP: ')
ip = '128.0.0.255'
nums = 0

print(ip.split('.'))

try:
    for i in ip.split('.'):
        # print(i)
        nums += 1
        # print(isinstance(int(i), int))
        if int(i) > 255:
            print('{} превышает 255'.format(i))
            break
        elif int(i) < 0:
            print('{} меньше нуля'.format(i))
            break
    if nums != 4:
        print('Адрес — это четыре числа, разделённые точками.')
    else:
        print('IP-адрес корректен.')
except:
    print(i, '— это не целое число.')
