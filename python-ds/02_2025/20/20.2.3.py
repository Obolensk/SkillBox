text = 'Здесь что-то написано'

ans = dict()

for sym in text:
    # print(sym)
    if sym in ans:
        ans[sym] += 1
    else:
        ans[sym] = 1

# print(sorted(ans))

for item in sorted(ans):
    print('{} : {}'.format(item, ans[item]))