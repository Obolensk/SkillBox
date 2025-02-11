#
my_dict = dict()

# num = int(input('Введите количество пар слов: '))
# for i in range(num):
#     print(i+1, end=' ')
#     couple = input('Пара: ').lower()
#     my_dict[couple.split()[0]] = couple.split()[1]


my_dict['привет'] = 'здравствуйте'
my_dict['печально'] = 'грустно'
my_dict['весело'] = 'радостно'
print(my_dict)

word_1 = 'интересно'
word_2 = 'здравствуйте'

def check(word):
    for i in my_dict:
        if word == i:
            print('Синонимом слова -{}- является -{}-'.format(word, my_dict[i]))
            break
        elif word == my_dict[i]:
            print('Синонимом слова -{}- является -{}-'.format(word, i))
            break
        else:
            print('Такого слова в словаре нет.')
            break

check(word_1)
check(word_2)
