data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

def search(passport, my_data):
    for data, person in my_data.items():
        if data == passport:
            print(person[1], person[0])

search((6000, 111111), data)
search((9000, 444444), data)