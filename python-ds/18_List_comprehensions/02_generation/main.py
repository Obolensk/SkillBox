# TODO здесь писать код


N = int(input('Введите длину списка: '))
list = [(1 if i % 2 ==0 else i % 5) for i in range(N)]

print(list)