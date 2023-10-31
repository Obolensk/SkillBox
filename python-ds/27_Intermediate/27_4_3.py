class Primes:
    def __init__(self, N):
        self.N = N
        self.num = 2

    def __iter__(self):
        return self

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def __next__(self):
        while self.num <= self.N:
            if self.is_prime(self.num):
                prime = self.num
                self.num += 1
                return prime
            self.num += 1
        raise StopIteration


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')

