# TODO здесь писать код

fst_text = input('Первая строка: ')
fst_str = []
for letter in fst_text:
    fst_str.append(letter)
# print(fst_str)

sec_text = input('Вторая строка: ')
sec_str = []
for letter in sec_text:
    sec_str.append(letter)
# print(sec_str)

def shift(str):
    new_str = [(str[i + 1] if i != (len(str) - 1) else str[0]) for i in range(len(str))]
    return new_str

shift_count = 0
my_str = fst_str[:]
for i in range(len(my_str)):
    my_str = shift(my_str)
    shift_count += 1
    # print(my_str)
    if my_str == sec_str:
        print('Первая строка получается из второй со сдвигом', shift_count)
        break
if shift_count == len(my_str):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига')