

file = open('numbers.txt', 'r', encoding='utf-8')

# print(file.read())
summ = 0

for i in file.read().split():
    summ += int(i)
    print(i)

print(summ)

ans = open('answer.txt', 'w', encoding='utf-8')
ans.write(str(summ))
ans.close()
