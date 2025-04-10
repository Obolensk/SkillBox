
file = open('zen.txt', 'r', encoding='utf-8')

my_list = file.read().split('\n')

for i in range(len(my_list)-1, -1, -1):
    print(my_list[i])
