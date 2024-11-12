string = input('Введите строку: ')
# string = 'гвозди:шурупы:гайки'
new_string = []

for i in string:
    if i == ':':
        i = '; '
    new_string.append(i)

print(''.join(new_string))
