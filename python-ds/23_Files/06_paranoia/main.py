# TODO здесь писать код

import os

abc_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(text, shift):
    text_list = [i for i in text]

    new_text = [(abc_list[(abc_list.index(text_list[i]) + shift) % 26] if text_list[i] != ' ' else ' ')
                for i in range(len(text_list))]

    return(''.join(new_text))

file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/06_paranoia/text.txt', 'r')
old_file = file.read()
print()

new_list = old_file.split('\n')
print(new_list)

s = 1
for string in new_list:
    new_file = open('C:/Users/e.menshaev/Desktop/Skillbox/python-ds/23_Files/06_paranoia/cipher_text.txt', 'a')
    new_file.write(ceasar(string, s))
    new_file.write('\n')
    s += 1
