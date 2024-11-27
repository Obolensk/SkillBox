# НЕ ГОТОВО ДЕБАЖИТЬ В PYCHARM

# 17.6.10


N = int(input('Кол-во чисел: '))
mylist = []

for _ in range(N):
    num = int(input('Число: '))
    mylist.append(num)

print(mylist)


def rev(mylist):
    reverse_list = []
    for i in reversed(mylist):
        reverse_list.append(i)
    return reverse_list


print(rev(mylist))

print()
ind = 0
new_list = []
new_list = list(mylist)


# Идея такая, пока список не станет "палиндромом", надо проверять на это сначала добавить нулевой элемнет и проверить ,
# потом добавить 1, 0 и проверить, потом добавить 2, 1, 0 и проверить и т.д.

print('\nnew_list = ', new_list)
print('rev(new_list) = ', rev(new_list))
print()
# mylist.append(555)
# print(mylist)
# print(new_list)

# for i in range(len(mylist), 0, -1):
#     print(i, end=' ')
#     print(len(mylist) - i)

# while new_list != rev(new_list):
if new_list != rev(new_list):
    for i in range(len(mylist)-1):
        new_list = list(mylist)
        added = []
        for a in range(i, -1, -1):
            new_list.append(mylist[a])
            added.append(mylist[a])
            print(a, end=' ')


print()
print('Последовательность:', mylist)
print('Нужно добавить чисел:', len(added))
print('\nnew_list = ', new_list)
print('Сами числа:', added)




