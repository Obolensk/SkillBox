student_info = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ')
new = dict()
print(student_info.split())
print(student_info)


for i in student_info.split():
    new['Имя'] = student_info.split()[0]
    new['Фамилия'] = student_info.split()[1]
    new['Город'] = student_info.split()[2]
    new['Место учебы'] = student_info.split()[3]
    new['Оценки'] = student_info.split()[4:]

for i in new:
    print('{} - {}'.format(i, new[i]))