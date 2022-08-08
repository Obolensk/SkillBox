# TODO здесь писать код
# my_list = input('Изначальный список: ')
my_list = [1, 2, 3, 4, 5]
print(my_list)
for i in range(len(my_list)):
    if my_list[i] > my_list[i-1]:
        my_list[i-1] = my_list[i]
    print(my_list[i])
print(my_list)
