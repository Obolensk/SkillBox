
first_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
second_lst = []
third_lst = []

print('\nСпособ 1')

for ind, num in enumerate(first_lst):
    lst = []
    if num % 2 == 0:
        lst.append(num)
        lst.append(num+1)
    if lst != []:
        second_lst.append(tuple(lst))
print(second_lst)



print('\nСпособ 2')

lst = []
for i in first_lst:
    if len(lst) < 2:
        lst.append(i)
    else:
        third_lst.append(tuple(lst))
        lst = []
        lst.append(i)
third_lst.append(tuple(lst))

print(third_lst)






#
# for num in range(len(first_lst)):
#     lst = []
#     for i in range(2):
#         lst.append(first_lst[num+i])
#     print(lst)
#     second_lst.append(tuple(lst))
#
# print(first_lst)
# print(second_lst)