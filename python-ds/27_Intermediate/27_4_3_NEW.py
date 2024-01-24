
class Primes():

    def __init__(self, N):
        self.N = N

    def __iter__(self):
        return self

    def __next__(self):
        count = 0
        for i in range(1, self.N):
            if self.N % i == 0:
                count += 1
        if count == 2:
            return self.N

prime_nums = Primes(2)
for i_elem in prime_nums:
    print(i_elem, end=' ')
