

my_str = 'so~mec~od~e'
# print(my_str)
# print(enumerate(my_str))

# a = enumerate(my_str)
# print(a)

my_list = []
for sym in my_str:
  my_list.append(sym)

answer = ''
for ind, val in enumerate(my_list):
  # print(ind, val)
  if val == '~':
    answer += str(ind) + ' '

print('Ответ:', answer)

# print(my_list)
# print(enumerate(my_list))


