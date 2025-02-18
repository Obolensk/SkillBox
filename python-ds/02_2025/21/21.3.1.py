
my_string = 'so~mec~od~e'

for sym in enumerate(my_string):
    if sym[1] == '~':
        print(sym[0], end=' ')

