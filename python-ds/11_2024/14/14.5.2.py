

def three_max(a, b, c):
    if c > max(a, b):
        return c
    else:
        return max(a, b)

print(three_max(12, 45, 5))
