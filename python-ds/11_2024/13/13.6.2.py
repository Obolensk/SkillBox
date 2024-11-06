

def positive():
    print('Положительное')

def negative():
    print('Отрицательное')


def test(a):
    if a >= 0:
        positive()
    else:
        negative()


test(-5)