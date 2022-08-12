guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код

ans = ''
while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    ans = input('Гость пришёл или ушёл? ')
    if ans == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    name = input('Имя гостя: ')
    if ans == 'пришёл':
        if len(guests) > 5:
            print('Прости,', name, ', но мест нет.')
        else:
            guests.append(name)
    if ans == 'ушёл':
        guests.remove(name)
        print('Пока,', name, '!')
