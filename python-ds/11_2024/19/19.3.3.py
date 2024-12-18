

congrats = input('Шаблон поздравления (туда вставляется ФИ и возраст): ')
names = input('ФИ людей (в одну строку, разделяются запятой): ')
# print(names.split())
ages = input('Возраст каждого человека (в одну строку через пробел): ')


for i in range(len(names.split(','))):
    print(congrats.format(name = names.split(',')[i], age = ages.split()[i]))
