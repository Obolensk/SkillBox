# TODO здесь писать код


with open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/24_Exceptions/04_registration/registrations.txt', 'r', encoding='utf-8') as file:
    for line in file:
        my_list = []
        for string in line.split():
            my_list.append(string)
        if len(my_list) == 3:
            if my_list[0].isalpha():
                if '@' in my_list[1] and '.' in my_list[1]:
                    if my_list[2].isdigit() and 10 < int(my_list[2]) < 99:
                        with open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/24_Exceptions/04_registration/registrations_good.log', 'a', encoding='utf-8') as good:
                            good.write(line)
                    else:
                        with open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/24_Exceptions/04_registration/registrations_bad.log', 'a', encoding='utf-8') as bad:
                            bad.write('Поле «Возраст» в строке {} НЕ является числом от 10 до 99'.format(line))
                            bad.write('\n')
                else:
                    with open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/24_Exceptions/04_registration/registrations_bad.log', 'a', encoding='utf-8') as bad:
                        bad.write('Поле «Имейл» в строке {} НЕ содержит @ и . (точку)'.format(line))
                        bad.write('\n')
            else:
                with open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/24_Exceptions/04_registration/registrations_bad.log', 'a', encoding='utf-8') as bad:
                    bad.write('Поле «Имя» в строке {} содержит НЕ только буквы'.format(line))
                    bad.write('\n')
        else:
            # print('По строке {} не хватает данных'.format(line))
            with open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/24_Exceptions/04_registration/registrations_bad.log', 'a', encoding='utf-8') as bad:
                bad.write('В строке {} не присутствуют все 3 поля'.format(line))

