# my_string = input('Введите строку: ')
my_string = 'hhqwerh'
sym = 'h'
result = []
frame = []



print('Развёрнутая последовательность между первым и последним h:', end='')

for i in range(len(my_string)):
    if my_string[i] == 'h':
        frame.append(i)

print(frame)
print(my_string[frame[0]+1:frame[-1]])
print(my_string[frame[-1]-1:frame[0]:-1])





