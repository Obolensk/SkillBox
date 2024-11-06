
def reverse(a):
    b = 0
    for i in range(1, len(str(a))+1):
        b = b * 10 + int(str(a)[-i])
    return (b)

reverse(123456)
def my_func():
    a = int(input('Введите число: '))
    if a == 0:
        print('Программа завершена!')
    else:
        print('Число наоборот:', reverse(a))
        my_func()

my_func()