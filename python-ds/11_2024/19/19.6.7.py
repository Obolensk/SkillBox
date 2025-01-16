

# ip = input('Введите IP: ')
ip = '125.45.68.123'
nums = 0

print(ip.split('.'))

for i in ip.split('.'):
    print(i)
    print(isinstance(int(i), int))
    if int(i) > 255:
        print('{} превышает 255'.format(i))
        break
    elif int(i) < 0:
        print('{} меньше нуля'.format(i))
        break
    nums += 1

if nums != 4:
    print('Адрес — это четыре числа, разделённые точками.')
else:
    print('IP-адрес корректен.')
