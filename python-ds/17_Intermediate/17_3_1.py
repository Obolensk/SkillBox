
main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]

main.extend(first_company)
main.extend(second_company)
main.extend(third_company)

print('Общий список задач: ', main)

not_done = 0
for i in main:
    if i == 0:
        not_done += 1

print('Кол-во невыполненных задач: ', not_done)
