
def factorial(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res

print(factorial(5))


def rec_fact(n):
    if n == 1:
        return 1
    return n * rec_fact(n - 1)

print()
print(rec_fact(5))