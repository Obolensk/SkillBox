#
# import random
# from xxsubtype import bench
#
# from Lib.test.test_inspect.inspect_fodder import after_closing
#
# # my_string = input('Введите строку: ')
#
# s = 'abacaba'
# # print(s)
# # print(s[:])
#
#
# def is_palindrome(string):
#     list_s = list()
#     rev_list_s = list()
#
#     for i in range(len(string)):
#         list_s.append(string[i])
#         rev_list_s.append(string[-i-1])
#     # print(list_s)
#     # print(rev_list_s)
#     if list_s == rev_list_s:
#         return True
#     else:
#         return False
#
#
# print(is_palindrome(s))
#
#
#
# before = 'ac'
# start_len = len(before)
#
# for i in range(len(before)**2):
#     ind = i
#     after = ''
#     while len(after) != start_len:
#         if len(before) > 0:
#             ind = random.randint(0, len(before)-1)
#         # else:
#         #     ind = 0
#             sym = before[ind]
#         print('ind = ', ind)
#         # print('before[ind] = ', before[ind])
#         before = before[:ind] + before[ind+1:]
#         after += sym
#     print('after = ', after)
#     if is_palindrome(after):
#         break
#
# if is_palindrome(after):
#     print('Можно сделать палиндромом')
# else:
#     print('Нельзя сделать палиндромом')
#
# print(before)
# print(after)


# Новый код помог написть Deep Seek
# я отправил ему старый год и текст ошибки, он описал почему возникала ошибка и исправил код.
# Супер инструмент

import random


def is_palindrome(string):
    # print(string)
    # print(string[::-1])
    return string == string[::-1]  # Упрощенная проверка на палиндром


before = 'aabc'
start_len = len(before)
found = False

for _ in range(len(before) ** 3):
    temp_before = list(before)  # Работаем с копией исходной строки
    after = ''

    while len(after) != start_len:
        if not temp_before:  # Если копия пуста, прерываем цикл
            break
        ind = random.randint(0, len(temp_before) - 1)
        sym = temp_before[ind]
        del temp_before[ind]
        after += sym

    if is_palindrome(after):
        found = True
        break

print(f"Можно сделать палиндромом" if found else "Нельзя сделать палиндромом")
