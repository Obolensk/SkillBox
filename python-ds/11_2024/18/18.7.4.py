
alphabet = 'abcdefg'

print('1.', end=' ')
print(alphabet[:])

print('2.', end=' ')
# print([alphabet[len(alphabet) - 1 - i] for i in range(len(alphabet))])
for i in range(len(alphabet)):
    print(alphabet[len(alphabet) - 1 - i], end='')

print('\n3.', end=' ')
for i in range(len(alphabet)):
    if i % 2 == 0:
        print(alphabet[i], end='')

print('\n4.', end=' ')
for i in range(len(alphabet)):
    if i % 2 != 0:
        print(alphabet[i], end='')

print('\n5.', end=' ')
print(alphabet[:1])

print('6.', end=' ')
print(alphabet[len(alphabet):len(alphabet)-2:-1])

print('7.', end=' ')
print(alphabet[3:4])

print('8.', end=' ')
print(alphabet[len(alphabet)-3:])

print('9.', end=' ')
print(alphabet[3:5])


print('10.', end=' ')
print(alphabet[len(alphabet)-3:len(alphabet)-5:-1])

