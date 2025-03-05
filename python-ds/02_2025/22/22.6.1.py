
num = int(input('Введите num: '))

def func(num):
    if num != 0:
        print(num)
        num -= 1
        func(num)

func(num)
print()

def rev_func(num, a = 1):
    if a != num + 1:
        print(a)
        a += 1
        rev_func(num, a)

rev_func(num)