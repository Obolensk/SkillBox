
l = [1, 2, 3, 4, 5]
f = [6, 7, 8, 9, 10]

def func(obj):
    while obj != []:
        print('Last Item is {} from LIST - {} was deleted'.format(obj[-1], obj))
        obj.pop()

func(l)
print()

def new_func(obj):
    while obj != []:
        print('First Item is {} from LIST - {} was deleted'.format(obj[0], obj))
        del obj[0]

new_func(f)