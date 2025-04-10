from Lib.operator import index

file = open('zen.txt', 'r', encoding='utf-8')
my_list = file.read().split('\n')
sym_list = ['.', ',', ':', ';', '!', '@', '#', '"', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+']

let_nums = 0
word_nums = 0
str_nums = 0
let_list = list()

for strings in my_list:
    for word in strings.split():
        for letter in word:
            let_list.append(letter.lower())
            let_nums += 1
        word_nums += 1
    str_nums += 1

print('\nКоличество букв в файле:', let_nums)
print('Количество слов в файле:', word_nums)
print('Количество строк в файле:', str_nums)
print()

count_dict = dict()

for let in let_list:
    count = 0
    for i in let_list:
        if let == i:
            count += 1
    count_dict[let] = count

new_dict = count_dict.copy()

print(count_dict.keys())
for item in count_dict:
    if item in sym_list:
        del new_dict[item]

print('count_dict = ', count_dict)
min_val = min(new_dict.values())
print('new_dict = ', new_dict)

for let, num in new_dict.items():
    if num == min_val and let not in sym_list:
        print('Наиболее редкая буква - {}, она встречается в тексте {} раз'.format(let, num))

# print(min_val)
