# пока непонятно как делать

#
#
# Пересмотреть начиная с 19.2 вообще не помню тему с шаблонами, возможно даже её и не было.
# А вообще начать смотреть с 19.1

while True:
    ip_address = input('Введите шаблон IP адреса, используйте {ip}: ')

    if '{ip}' in ip_address:
        break
    print('Ошибка шаблона, отсутствует конструкция {ip}')

eventual_ip = []
ip = 0
while len(eventual_ip) < 4:
    ip = int(input('Ведите число от 0 до 255 (включительно): '))
    if 0 <= ip <= 255:
        eventual_ip.append(ip)
    else:
        print('Внимание, ошибка!!!')
        ip = int(input('Ведите число от 0 до 255 (включительно): '))

print('eventual_ip = ', eventual_ip)

for i in eventual_ip:
   print(ip_address.format(ip=i), end='.')



# print(ip_address)




