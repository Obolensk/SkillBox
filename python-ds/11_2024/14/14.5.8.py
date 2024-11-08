

x = float(input('Введите х = '))
precision = float(input('Введите точность = '))
new_pres = 0

# x = 5
# precision = 4

for i in range(int(1/precision)):
    new_pres += 1
print('new_pres = ', new_pres)

def fact(n):
    if n == 0:
        return 1
    else:
        for i in range(1, n):
            n *= i
        return n

def degree(a, b):
    if b == 0:
        return 1
    else:
        x = a
        for i in range(b-1):
            x *= a
        return x

result = 0

for n in range(10):
    result += degree(-1, n) * (degree(x, 2 * n) / (fact(2 * n)))

print('result = ', round(result, new_pres))

