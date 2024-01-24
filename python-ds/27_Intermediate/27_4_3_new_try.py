class Primes:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1

        while True:
            if self.current > 2 and all(self.current % i != 0 for i in range(2, int(self.current ** 0.5) + 1)):
                if self.current > self.max_num:
                    raise StopIteration
                else:
                    prime = self.current
                    self.current += 1
                    return prime
            else:
                self.current += 1


prime_nums = Primes(1000)

for i_elem in prime_nums:
    print(i_elem, end=' ')