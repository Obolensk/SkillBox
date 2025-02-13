
import random
from xxsubtype import bench

from Lib.test.test_inspect.inspect_fodder import after_closing

# my_string = input('Введите строку: ')

s = 'abacaba'
# print(s)
# print(s[:])


def is_palindrome(string):
    list_s = list()
    rev_list_s = list()

    for i in range(len(string)):
        list_s.append(string[i])
        rev_list_s.append(string[-i-1])
    # print(list_s)
    # print(rev_list_s)
    if list_s == rev_list_s:
        return True
    else:
        return False


print(is_palindrome(s))


before = 'abcd'
start_len = len(before)
after = ''
while len(after) != start_len:
    ind = random.randint(0, len(before)-1)
    sym = before[ind]
    before = before[:ind] + before[ind+1:]
    print('before = ', before)
    if sym in after:
        continue
    else:
        after += sym
    print('after = ', after)
print(before)
print(after)



