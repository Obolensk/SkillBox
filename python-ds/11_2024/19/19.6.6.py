# Введите строку: aaAAbbсaaaA
#
# Закодированная строка: a2A2b2с1a3A1

my_str = 'aaAAbbсaaaA'
ans = []
new = []

count = 1
for i in range(len(my_str)):
    if my_str[i] == my_str[i-1]:
        count += 1
    else:
        print(my_str[i-1], end='')
        print(count, '',end='')
        ans.append(my_str[i-1])
        ans.append(count)
        count = 1

print()
print(ans)

for i in range(len(ans)):
    if i != 0 or i != 1:
        print(ans[i], end='')
        new.append(ans[i])
    else:
        print(ans[i - 2], end='')
        new[-1] = ans[1]
        new[-2] = ans[0]

print(new)
#
# #
# count = 1
# for i in range(1, len(my_str)+1):
#     if my_str[i-1] == my_str[i-2]:
#         count += 1
#     # elif i == len(my_str):
#     #     if my_str[i] == my_str[i - 1]:
#     #         count += 1
#     #     else:
#     #         count = 1
#     else:
#         print(my_str[i-2], end='')
#         print(count, '',end='')
#         count = 1
#

