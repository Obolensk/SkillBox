
# word = input('Введите слово: ')
word = 'привет'
my_list = list(word)
answer = 0

for i_word in word:
    count = 0
    for i_list in my_list:
        if i_list == i_word:
            count += 1
    if count == 1:
        answer += 1

print(answer)
