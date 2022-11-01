list_1 = ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']

list_2 = ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']

dict_1 = {}
dict_2 = {}

for ind, val in enumerate(list_1):
    dict_1[ind] = val

print(dict_1)

for ind, val in enumerate(list_2):
    dict_2[ind] = val

print(dict_2)
