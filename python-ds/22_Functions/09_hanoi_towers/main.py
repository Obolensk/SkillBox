# TODO здесь писать код


def disc(n, a, b, c):
    if n==1:
        print('Диск 1 со стержня {} на стержень {}'.format(a, b))
        return 
    else:
      disc(n-1, a, c, b)
      print('Диск {} со стержня {} на стержень {}'.format(n, a, b))
      disc(n-1, c, b, a)
          
disc(5, 1, 3, 2)
