
orders_num = int(input('Введите кол-во заказов: '))
my_dict = dict()
for i in range(orders_num):
    my_dict[i] = dict()
print(my_dict)

for i in range(orders_num):
    print(i+1, end=' ')
    order_info = input('заказ ')
    if i == 0:
        my_dict[order_info.split()[i]] = my_dict.pop(i)
    else:
        my_dict.pop(i)
    print(my_dict.keys())
    # print('order_info.split()[1] in my_dict[order_info.split()[0]] = ', order_info.split()[1] in my_dict[order_info.split()[0]])
    if order_info.split()[0] in my_dict.keys():
        if order_info.split()[1] in my_dict[order_info.split()[0]]:
            my_dict[order_info.split()[0]][order_info.split()[1]] += int(order_info.split()[2])
        else:
            my_dict[order_info.split()[0]][order_info.split()[1]] = int(order_info.split()[2])
    # print('my_dict[order_info.split()[0]] = ', my_dict[order_info.split()[0]])
    # print('order_info.split()[1] in my_dict[order_info.split()[0]] = ', order_info.split()[1] in my_dict[order_info.split()[0]])
    # print('my_dict[order_info.split()[0]][order_info.split()[1]] = ', my_dict[order_info.split()[0]][order_info.split()[1]])
    # print('order_info.split()[1] = ', order_info.split()[1])
    # print('order_info.split()[2] = ', order_info.split()[2])
    print(my_dict)
print(my_dict)