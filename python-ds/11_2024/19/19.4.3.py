str_1 = 'ПитоН - этО хорошО'
str_2 = 'ПиТоН - ЭтО УДоБнО'

# print(str_1[0])
# print(str_1[0].lower())
# print(str_1[0].islower())

def reg(str):
    l = 0
    u = 0
    for i in str:
        if i.islower():
            l += 1
        else:
            u += 1
    if l > u:
        print(str.lower())
    else:
        print(str.upper())

reg(str_1)
reg(str_2)
