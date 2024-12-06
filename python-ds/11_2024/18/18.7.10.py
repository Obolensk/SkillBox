
letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
           "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

msg = 'это питон'
shift = 3
# answer = ''
#
# for i in range(len(msg)):
#     if msg[i] == ' ':
#         answer += ' '
#     else:
#         answer += letters[(letters.index(msg[i]) + shift) % len(letters)]

answer = [' ' if msg[i] == ' ' else letters[(letters.index(msg[i]) + shift) % len(letters)] for i in range(len(msg))]


print('Зашифрованное сообщение: ', end='')

for let in answer:
    print(let, end='')
