
def rev(mylist):
    reverse_list = []
    for i in reversed(mylist):
        reverse_list.append(i)
    return reverse_list


mylist = [1, 2, 3, 3, 2, 1]
print(rev(mylist))

if mylist == rev(mylist):
    print('Палиндром')
else:
    print('НЕ палиндром')