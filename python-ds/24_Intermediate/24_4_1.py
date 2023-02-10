
with open('people.txt', 'r', encoding='utf-8') as file:
    for name in file.read().split():
        for lit in name