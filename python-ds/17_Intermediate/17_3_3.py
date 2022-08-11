
pack_nums = int(input('Кол-во пакетов: '))
errors = 0
total_errors = 0
error_files = 0
msg = []
total_msg = []

for pack in range(pack_nums):
    print('Пакет номер', pack+1)
    for i in range(4):
        print(i+1, 'бит:', end='')
        bit = int(input(' '))
        msg.append(bit)
        if bit != 0 and bit != 1:
            errors += 1
    print('errors = ', errors)
    if errors <= 1:
        total_msg.extend(msg)
    else:
        error_files += 1
    errors = 0
    print()

for i in total_msg:
    if i != 0 and i != 1:
        total_errors += 1

print('Полученное сообщение: ', total_msg)
print('Кол-во ошибок в сообщении: ', total_errors)
print('Кол-во потерянных пакетов: ', error_files)
