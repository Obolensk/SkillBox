

def count_letters(text, number, letter):
    let_count = 0
    num_count = 0
    my_list = []
    for i in text:
        if i == str(number):
            num_count += 1
        elif i == letter:
            let_count += 1
    print('Количество цифр "{}" в тексте равняется {}'.format(number, num_count))
    print('Количество букв "{}" в тексте равняется {}'.format(letter, let_count))

count_letters('Привет 1 Андрей 4 приевет 5', 5,'в')


# #
# text = 'Привет'
# print(text)
# my_list = []
# for i in text:
#     my_list.append(i)
#
# print(my_list)