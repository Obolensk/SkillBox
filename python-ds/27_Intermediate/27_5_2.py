

def gen():
    summ = 0
    with open('C:/Users/ASUS/Desktop/SkillBox/python-ds/27_Intermediate/numbers.txt', 'r') as file:
        for i in file.read().split():
            # print(i.split(" '\n'"))
            # if int(i[0]) == int:
            if i != '\n':
                # print('summ = ', summ)
                # print('i = ', i)
                summ += int(i)
                yield summ

print(gen())

for i in gen():
    print(i)
