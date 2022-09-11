# TODO здесь писать код

my_str = input('Введите строку: ')
h_list = [i for i in range(len(my_str)) if my_str[i] == 'h']

print('Развёрнутая последовательность между первым и последним h:', my_str[h_list[-1]-1:h_list[0]:-1])


