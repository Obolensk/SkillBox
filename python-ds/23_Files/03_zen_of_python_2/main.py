# TODO здесь писать код

new_file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/02_zen_of_python/zen.txt', 'r',
                encoding='UTF-8')

let = 0
words = 0
strs = 0
r_let = 10
l_count = 0

zen = new_file.read()
zen_list = []

for l in zen:
    let += 1
print('Количество букв в файле:', let)

for w in zen.split():
    words += 1
print('Количество слов в файле:', words)

for s in zen.split('\n'):
    strs += 1
print('Количество строк в файле:', strs)

for i in zen:
    zen_list.append(i)

# print(zen_list)
# print((len(zen_list)))


for a in range(len(zen_list)):
    # print('Для a = ',zen_list[a] , 'str(a).isalpha() = ', str(zen_list[a]).isalpha())
    if str(zen_list[a]).isalpha():
        for b in range(len(zen_list)):
            if zen_list[a].lower() == zen_list[b].lower():
                l_count += 1
        # print('Количество букв ', zen_list[a].lower(), 'равняется', l_count)
        if l_count < r_let:
            r_let = l_count
            my_let = zen_list[a].lower()
        l_count = 0

print('Наиболее редкая буква в файле:',my_let , 'Она встречается всего-то навсего', r_let, 'раза! Вот так-то!!!')


