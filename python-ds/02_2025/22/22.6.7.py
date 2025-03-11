
def my_sum(*args):
    sum = 0
    for elem in args:
        if isinstance(elem, list) or isinstance(elem, tuple):
            for i in elem:
                sum += i
        else:
            sum += elem
    return sum





print(my_sum([1, 2], [3, 4], (5, 7), 10, 32.0))