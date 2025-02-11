
orders_num = int(input('Введите кол-во заказов: '))
my_dict = dict()

for i in range(orders_num):
    print(i+1, end=' ')
    order_info = input('заказ ')
    my_dict[order_info.split()[0]] = dict()
    # print(order_info.split()[0] in my_dict)
    print(order_info.split()[1], my_dict[order_info.split()[0]].values())
    print(order_info.split()[0])
    print(my_dict['Иванов'])
    print('my_dict[order_info.split()[0]] = ', my_dict[order_info.split()[0]])
    if order_info.split()[0] in my_dict and order_info.split()[1] in my_dict.values():
        my_dict[order_info.split()[0]][order_info.split()[1]] += order_info.split()[2]
    else:
        my_dict[order_info.split()[0]][order_info.split()[1]] = order_info.split()[2]

print(my_dict)