
players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

print(1)
# print(len(players_dict))
# print(players_dict[1])

for s_name in range(1, len(players_dict)+1):
    if players_dict[s_name]['team'] == 'A' and players_dict[s_name]['status'] == 'Rest':
        print(players_dict[s_name]['name'], end=', ')

print()
print(2)

for s_name in range(1, len(players_dict)+1):
    if players_dict[s_name]['team'] == 'B' and players_dict[s_name]['status'] == 'Training':
        print(players_dict[s_name]['name'], end=', ')

print()
print(3)

for s_name in range(1, len(players_dict)+1):
    if players_dict[s_name]['team'] == 'C' and players_dict[s_name]['status'] == 'Travel':
        print(players_dict[s_name]['name'], end=', ')

