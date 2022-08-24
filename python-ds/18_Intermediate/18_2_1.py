
left = int(input('Левая граница: '))
right = int(input('Правая граница: '))

cubes = [i ** 3 for i in range(left, right + 1)]

squares = [i ** 2 for i in range(left, right + 1)]

print('Список кубов чисел в диапазоне от', left, 'до', right, ':', cubes)
print('Список квадратов чисел в диапазоне от', left, 'до', right, ':', squares)