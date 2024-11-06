low = int(input('Нижняя граница: '))
hi = int(input('Верхняя граница: '))
step = int(input('Шаг: '))


print('C', end='\t')
print('F')
cels = 0

for c in range(low, hi, step):
    print(c, '\t', int(c * 1.8 + 32))
    cels = c

if cels != hi:
    print(hi, '\t', int(hi * 1.8 + 32))
