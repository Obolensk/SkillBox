#
# def move(n, start=1, final=3, prom=2):
#     if n == 1:
#         print('Переложить диск 1 со стержня номер {} на стержень номер {}'.format(start, final))
#     else:
#         move(n-1)
#         print('Переложить диск {} со стержня номер {} на стержень номер {}'.format(n, start, prom))
#         move(n-1, final, prom)
#
#
#
# move(2)


def disc(n, start, final, prom):
    if n == 1:
        print('\nДиск 1 со стержня {} на стержень {}'.format(start, final))
        return
    else:
        disc(n - 1, start, prom, final)
        print('Диск {} со стержня {} на стержень {}'.format(n, start, final))
        disc(n - 1, prom, final, start)


disc(3, 1, 3, 2)