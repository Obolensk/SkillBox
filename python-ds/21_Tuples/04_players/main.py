players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# TODO здесь писать код

lst_1 = []
lst_2 = []
for key in players:
  for name in key:
    lst_1.append(name)
  for sym in players[key]:
    lst_1.append(sym)
  lst_2.append(tuple(lst_1))
  lst_1 = []

print(lst_2)
