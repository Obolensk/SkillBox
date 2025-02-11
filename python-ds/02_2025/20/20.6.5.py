
text = 'Здесь что-то написано'

ans = dict()

for sym in text:
    if sym in ans:
        ans[sym] += 1
    else:
        ans[sym] = 1

my_set = set(ans.values())
my_dict = dict()
for num in my_set:
    my_list = []
    for item in ans:
        if num == ans[item]:
            my_list.append(item)
        my_dict[num] = my_list

for i in my_dict:
    print('{} : {}'.format(i, my_dict[i]))


# Инвертированный словарь частот:
# 1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']
# 2 : ['с', ' ', 'т', 'н', 'а']
# 3 : ['о']