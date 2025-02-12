
orders_num = int(input('Введите кол-во заказов: '))
my_dict = dict()
# for i in range(orders_num):
#     my_dict[i] = dict()
#     my_dict[i][i] = dict()
# print(my_dict)
# print(my_dict[5])

#
# for i in range(orders_num):
#     print(i+1, end=' ')
#     order_info = input('заказ ')
#
#     if order_info.split()[0] not in my_dict:
#         # order_info.split()[0] = dict()
#         my_dict[order_info.split()[0]] = dict()
#         my_dict[order_info.split()[0]].update({order_info.split()[1]: int(order_info.split()[2])})
#
#     else:
#         if order_info.split()[1] not in my_dict[order_info.split()[0]]:
#             # my_dict[order_info.split()[0]][1] = order_info.split()[2]
#             my_dict[order_info.split()[0]][order_info.split()[1]].update({order_info.split()[1]: int(order_info.split()[2])})
#         else:
#             my_dict[order_info.split()[0]][1] += order_info.split()[2]
#
#         my_dict[order_info.split()[0]][order_info.split()[1]] += int(order_info.split()[2])
#
# print(my_dict)
#


for i in range(orders_num):
    print(i+1, end=' ')
    order_info = input('заказ ')

    # Если фамилии нет в списке
    if order_info.split()[0] not in my_dict.keys():
        print('фамилии нет в списке')
        my_dict[order_info.split()[0]] = dict()
        my_dict[order_info.split()[0]][order_info.split()[1]] = int(order_info.split()[2])
        continue
        print(my_dict)

        # Если пиццы нет у фамилии
        if order_info.split()[1] not in my_dict[order_info.split()[0]]:
            print('пиццы нет у фамилии')
            my_dict[order_info.split()[0]][order_info.split()[1]] = int(order_info.split()[2])
            continue
        # Если пицца есть у фамилии
        else:
            print('пицца есть у фамилии')
            my_dict[order_info.split()[0]][order_info.split()[1]] += int(order_info.split()[2])
            continue

    # Если фамилия есть в списке
    else:
        print('фамилия есть в списке')

        # Если пиццы нет у фамилии
        if order_info.split()[1] not in my_dict[order_info.split()[0]]:
            print('пиццы нет у фамилии')
            # print(order_info.split()[0][1])
            # print(my_dict[order_info])
            my_dict[order_info.split()[0]][order_info.split()[1]] = int(order_info.split()[2])
            continue

        # Если пицца есть у фамилии
        else:
            print('пицца есть у фамилии')
            my_dict[order_info.split()[0]][order_info.split()[1]] += int(order_info.split()[2])
#     print(my_dict)
#     print(my_dict.keys())
print(my_dict)
#
#
# if 5 not in my_dict:
#     my_dict[5] = dict()
#     my_dict[5].update({6: 7})
#     if 8 not in my_dict[5]:
#         my_dict[5].update({8: 9})
#
# else:
#     my_dict[5].update({6: 7})
#
# print(my_dict)
# print(my_dict[5])








#
# В базе данных интернет-магазина PizzaTime хранятся данные о том, кто, что и сколько заказывал у них
# в определённый период. Вам нужно структурировать эту информацию, а также понять,
# сколько всего пицц купил каждый заказчик.
# На вход в программу подаётся N заказов.
# Каждый заказ представляет собой строку вида «Покупатель — название пиццы — количество заказанных пицц».
# Реализуйте код, который выводит список покупателей и их заказов по алфавиту.
# Учитывайте, что один человек может заказать одно и то же несколько раз.
# Пример:
# Введите кол-во заказов: 6
# 1 заказ: Иванов Пепперони 1
# 2 заказ: Петров Де-Люкс 2
# 3 заказ: Иванов Мясная 3
# 4 заказ: Иванов Мексиканская 2
# 5 заказ: Иванов Пепперони 2
# 6 заказ: Петров Интересная 5
#
# Иванов:
#     Мексиканская: 2
#     Мясная: 3
#     Пепперони: 3
# Петров:
#     Де-Люкс: 2
#     Интересная: 5