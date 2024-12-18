
string = 'я е'
print(string.split())

max = 0
for word in string.split():
    lengh = 0
    for sym in word:
        lengh += 1
    if lengh > max:
        answer = word
        max = lengh

print('\nСамое длинное слово: {} \nДлина этого слова: {}'.format(answer, max))