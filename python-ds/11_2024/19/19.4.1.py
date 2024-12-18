
letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
           "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

msg = 'это Питон'
shift = 3

answer = [' ' if msg[i].lower() == ' '
          else letters[(letters.index(msg[i].lower()) + shift) % len(letters)]
          for i in range(len(msg))]

print('Зашифрованное сообщение: ', end='')

for let in answer:
    print(let, end='')
