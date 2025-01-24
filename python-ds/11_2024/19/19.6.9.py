# Для первого примера этот код работает
#
# sym = ['.', ',', ':', ';', '?', '!', ' ']
# new_sym = []
#
# text = 'Это задание очень! простое.'
# print(text[3], text[4], text[5])
# string = text.split()
# print(string)
# new_list = []
#
# for word in string:
#
#     for i in range(len(word)-1, -1, -1):
#         if word[i] in sym:
#             new_sym.append(word[i])
#         else:
#             new_list.append(word[i])
#             # print(word[i], end='')
#     if new_sym != []:
#         new_list.append(new_sym[0])
#         new_sym.pop(-1)
#     new_list.append(' ')
#
# print(new_list)
#
# for i in new_list:
#     print(i, end='')




sym = ['.', ',', ':', ';', '?', '!', ' ']
new_sym = []

text = 'Хотя ,. возм:ожно и нет.'
print(text[3], text[4], text[5])
string = text.split()
print(string)
new_list = []

for word in string:

    for i in range(len(word)-1, -1, -1):
        if word[i] in sym:
            new_sym.append(word[i])
        else:
            new_list.append(word[i])
            # print(word[i], end='')
    if new_sym != []:
        new_list.append(new_sym[0])
        new_sym.pop(0)
    new_list.append(' ')

print(new_list)

for i in new_list:
    print(i, end='')