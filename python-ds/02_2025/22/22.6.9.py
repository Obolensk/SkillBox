

def move(n, x=1, y=3):
    lst_1 = [i+1 for i in range(n)]
    lst_2 = []
    lst_3 = []
    print('lst_1 = ', lst_1, end=' / ')
    print('lst_2 = ', lst_2, end=' / ')
    print('lst_3 = ', lst_3)
    print('Задача переместить {} дисков со стрежня {} на стержень {}'.format(n, x, y))
    lst_2.append(lst_1[-1])
    lst_1.remove(lst_1[-1])
    lst_3.append(lst_1[-1])
    lst_1.remove(lst_1[-1])
    lst_3.append(lst_2[-1])
    lst_2.remove(lst_2[-1])
    print('lst_1 = ', lst_1, end=' / ')
    print('lst_2 = ', lst_2, end=' / ')
    print('lst_3 = ', lst_3)




# n = int(input('Введите количество дисков: '))
n = 3

move(n)