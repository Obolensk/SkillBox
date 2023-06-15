
with open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/26_Intermediate/numbers.txt', 'r', encoding='utf-8') as file:
    for couple in file:
        print(couple.split())
        if int(couple.split()[0]) >= int(couple.split()[1]):
            print(int(couple.split()[0])/int(couple.split()[1]))
        else:
            raise Exception('DivisionError (нельзя делить большее на меньшее)')


