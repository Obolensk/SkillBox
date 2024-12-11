task = []
# text = []
word = str()

def word_count(word, text):
    count = 0
    for i in text:
        if word == i:
            count += 1
    return count

for i in range(1, 4):
    print('Введите', i, 'слово: ', end='')
    word = input()
    task.append(word)

# print()
# while word != 'end':
#     word = input('Слово из текста: ')
#     text.append(word)

print()
text = input('Введите текст: ')
print(text.split())

print('\nПодсчет слов в тексте')

print(task[0], ':', word_count((task[0]), text.split()))
print(task[1], ':', word_count((task[1]), text.split()))
print(task[2], ':', word_count((task[2]), text.split()))