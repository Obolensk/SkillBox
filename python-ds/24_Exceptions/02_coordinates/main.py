import random

def f(x, y):
    x += random.randint(0, 5)
    y += random.randint(0, 10)
    return x / y

def f2(x, y):
    x -= random.randint(0, 5)
    y -= random.randint(0, 10)
    return y / x

with open('coordinates.txt', 'r', encoding='utf-8') as file:
    for line in file:
        nums_list = line.split()
        try:
            res1 = f(int(nums_list[0]), int(nums_list[1]))
        except Exception:
            print("Что-то пошло не так с первой функцией")
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
        except:
            print("Что-то пошло не так со второй функцией")
        number = random.randint(0, 100)
        with open('result.txt', 'a', encoding='utf-8') as file_2:
            my_list = sorted([res1, res2, number])
            for item in my_list:
                file_2.write(str(item))
                file_2.write(' ')
            file_2.write('\n')


# TODO отредактировать и исправить программу
