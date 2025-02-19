
players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

total = []

for keys, values in players.items():
    lst = []
    for key in keys:
        lst.append(key)
    for value in values:
        lst.append(value)
    total.append(tuple(lst))

print(total)

