# TODO здесь писать код

pos = 6

n = 1
fibo = [1, 1, 2]

for i in range(3, 20):
  fibo.append(fibo[i-1] + fibo[i-2])
# print(fibo)

def npf(n):
  print('Число:', fibo[n-1])

num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
npf(num_pos)


