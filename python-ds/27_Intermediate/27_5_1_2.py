
def Primes(max_num):
    current = 1
    while True:
        if current > 2 and all(current % i != 0 for i in range(2, int(current ** 0.5) + 1)):
            if current > max_num:
                # raise StopIteration
                break
            else:
                prime = current
                current += 1
                yield prime
        else:
            current += 1

prime_nums = Primes(100)

for i_elem in prime_nums:
    print(i_elem)