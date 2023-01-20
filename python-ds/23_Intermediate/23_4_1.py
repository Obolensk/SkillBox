nums = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/numbers.txt', 'r')
my_nums = nums.read()
# print(my_nums)
total = 0
# list = []

for i in my_nums.split():
    total += int(i)
    # print(i, end='')
    # list.append(i)

# print(list)
# print()
# print(total)

result = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Intermediate/answer.txt', 'w')
result.write(str(total))

nums.close()