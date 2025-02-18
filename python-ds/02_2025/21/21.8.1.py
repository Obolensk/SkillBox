students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def interests(dict):
    lst = []
    sur_len = 0
    for key, value in dict.items():
        lst.extend(value['interests'])
        sur_len += len(value['surname'])
    return lst, sur_len

print('\nЗадание 1')
pairs = dict()
for id, student in students.items():
    pairs[id] = student['age']
print(pairs)

print('\nЗадание 2')
print(interests(students))

print('\nЗадание 3')
for item in zip(interests(students)):
    print(item)
