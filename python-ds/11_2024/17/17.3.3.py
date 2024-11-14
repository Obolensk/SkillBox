
pack_nums = int(input('Введите количество пакетов: '))
message = []
lost_packs = 0

for i_pack in range(pack_nums):
    print('\nПакет №', i_pack+1)
    pack = []
    errors = 0
    for i in range(4):
        print(i, 'бит:', end=' ')
        byte = int(input(''))
        pack.append(byte)
        if byte == -1:
            errors += 1
    if errors > 1:
        lost_packs +=1
        print('Много ошибок в пакете!')
    else:
        message.extend(pack)

print('Полученное сообщение:', message)
print('Кол-во ошибок в сообщении:', message.count(-1))
print('Кол-во потерянных пакетов:', lost_packs)