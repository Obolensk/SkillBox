# Введите зашифрованное сообщение: shacnidw
# Расшифрованное сообщение: sandwich


code = input('Введите зашифрованное сообщение: ')
decode = ''

# print(code[0])
# print(code[1])
# print(code[2])
# print(code[3])
# print(code[4])
# print(code[5])
# print(code[6])
#
# print(code[-1]+code[-2]+code[-3]+code[-4]+code[-5]+code[-6]+code[-7])

# for i in range(len(code)):
#     print(code[i], end=' - ')

for i in range(0, len(code), 2):
    print(code[i], end=' - ')
    # print(code[-(i+1)], end=' - ')

for i in range(0, len(code), 2):
    print(code[-(i+1)], end=' - ')
    # print(code[-(i+1)], end=' - ')

