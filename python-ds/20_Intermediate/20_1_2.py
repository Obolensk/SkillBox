student_info = input('Введите информацию о студенте через пробел\n '
                     '(имя, фамилия, город, место учёбы, оценки): ')
student_list = student_info.split()

student_dict = dict()

# print(student_info)
# print(student_list)

student_dict['Имя'] = student_list[0]
student_dict['Фамилия'] = student_list[1]
student_dict['Город'] = student_list[2]
student_dict['Место учебы'] = student_list[3]
student_dict['Оценки'] = []

for i_nums in student_list[4:]:
    student_dict['Оценки'].append(i_nums)

for i in student_dict:
    print(i, ' = ', student_dict[i])


# print(student_dict)