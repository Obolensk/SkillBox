h = int(input('Введите высоту пирамидки: '))
for col in range(h):
    for row in range(h*2-2):
        if row == h - 1 - col:
            print('#'*(1+col*2), end='')
        else:
            print(' ', end='')
    print()
