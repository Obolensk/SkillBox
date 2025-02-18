tup = (1, 2, 'dsf', ['f', 'g', 555], 12, 'd', 44)

print(tup)

def is_prime(a):
    count = 0
    for i in range(1, a+1):
        if a % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

def func(col):
    lst = []
    for ind, val in enumerate(col):
        if is_prime(ind):
            lst.append(val)
    print(lst)


print()
func(tup)

