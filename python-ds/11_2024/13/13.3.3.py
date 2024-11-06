n = int(input('Введите N: '))
# n = 3

def isPrime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0 and n != 2:
            count += 1
    if count == 2:
        return True
    else:
        return False

# print(isPrime(n))

prime_count = 0
for i in range(1, n+1):
    if isPrime(i):
        prime_count += 1

print('В последовательности из {} чисел, {} являются простыми!'.format(n, prime_count))