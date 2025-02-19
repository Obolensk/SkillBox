
people = {
    'Сидоров Никита': 35,
    'Иванова Алина': 34,
    'Петров Павел': 10,
    'Иванов Иван': 35,
    'Петрова Алина': 34,
    'Павлов Павел': 10,
    'Иванов Никита': 35,
    'Павлова Алина': 34,
    'Иванов Павел': 10,
    'Петров Никита': 35,
    'Сидорова Алина': 34,
    'Сидоров Павел': 10,

}

# print(people)

surname = input('Введите фамилию: ')
start_sur = surname[:5].lower()
# print(start_sur)

for person, age in people.items():
    if person.lower().startswith(start_sur):
        print(person, age)


