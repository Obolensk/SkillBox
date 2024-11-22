
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
answer = ''


while answer != 'Пора спать':
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    answer = input('Гость пришёл или ушёл? ')
    if answer == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            print('Привет,', name)
            guests.append(name)
        else:
            print('Прости,', name + ', но мест нет.')
    elif answer == 'ушёл':
        name = input('Имя гостя: ')
        print('Пока,', name)
        guests.remove(name)


print('Вечеринка закончилась, все легли спать.')