# TODO здесь писать код


def func(n):
  if n == 0:
    return n
  else:
    func(n - 1)
  print(n)

num = int(input('Введите num: '))
func(num)
