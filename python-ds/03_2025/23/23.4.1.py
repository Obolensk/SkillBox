
file = open('numbers.txt', 'r')
sum = 0
for num in file:
    # print(num)
    sum += int(num)

# print(sum)

ans = open('answer.txt', 'w')
ans.write(str(sum))
ans.close()