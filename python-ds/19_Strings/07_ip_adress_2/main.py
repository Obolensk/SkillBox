# TODO здесь писать код

while True:
    ip_adress = input('Введите IP: ').split('.')
    print(ip_adress)
    num_count = 0
    for num in ip_adress:
        num_count += 1
        if not num.isdigit():
            print('{0} — это не целое число'.format(num))
            break
        elif int(num) < 0:
            print('{0} меньше 0'.format(num))
            break
        elif int(num) > 255:
            print('{0} првышает 255'.format(num))
            break
        elif not num.isdigit():
            print('{0} — это не целое число'.format(num))
            break
        # elif num_count != 4:
        #     print('Адрес — это четыре числа, разделённые точками.')
        else:
            print('IP-адрес корректен.')

    break