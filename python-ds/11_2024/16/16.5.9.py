
# 16.5.9

my_list = [1, 4, -3, 0, 10, 15, 28, 99, -25, -2, 54, 8, -8, -69, 45, 78, -63, 52, -89, -1, 3, 55, 24, -47, -22, -6, 21, 61, 5]
print(my_list)

for _ in range(len(my_list)):
    for i in range(len(my_list)-1):
        a = my_list[i]
        b = my_list[i+1]
        if a > b:
            my_list[i] = b
            my_list[i+1] = a

print(my_list)