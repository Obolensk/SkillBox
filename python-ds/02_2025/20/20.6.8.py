import random

# ans = []
max_num = int(input('Введите максимальное число: '))
my_num = random.randint(0, max_num)
print(my_num)
while True:
    my_ans = input('Нужное число есть среди вот этих чисел: ')
    ans = my_ans.split()
    print(ans)
    if my_ans == '000':
        ans = []
        for i in range(3):
            a = random.randint(0, max_num)
            if a != my_num and a not in ans:
                ans.append(a)
        ans.append(my_num)
        print('Артём мог загадать следующие числа: {}'.format(ans))
        break

    elif str(my_num) in ans:
        print('Ответ Артёма: Да')
    else:
        print('Ответ Артёма: Нет')











print(my_num)