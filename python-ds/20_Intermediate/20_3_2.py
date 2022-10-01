players_dict = {
  1: {
    'name': 'Vanya',
    'team': 'A',
    'status': 'Rest'
  },
  2: {
    'name': 'Lena',
    'team': 'B',
    'status': 'Training'
  },
  3: {
    'name': 'Maxim',
    'team': 'C',
    'status': 'Travel'
  },
  4: {
    'name': 'Egor',
    'team': 'C',
    'status': 'Rest'
  },
  5: {
    'name': 'Andrei',
    'team': 'A',
    'status': 'Training'
  },
  6: {
    'name': 'Sasha',
    'team': 'A',
    'status': 'Rest'
  },
  7: {
    'name': 'Alina',
    'team': 'B',
    'status': 'Rest'
  },
  8: {
    'name': 'Masha',
    'team': 'C',
    'status': 'Travel'
  }
}

print()
print('1. Все члены команды из команды А, которые отдыхают.')
print()
for i in players_dict:
  if players_dict[i].get('status') == 'Rest' and players_dict[i].get(
      'team') == 'A':
    print(players_dict[i].get('name'))

print()
print('2. Все члены команды из группы B, которые тренируются.')
print()
for i in players_dict:
  if players_dict[i].get('status') == 'Training' and players_dict[i].get(
      'team') == 'B':
    print(players_dict[i].get('name'))

print()
print('3. Все члены команды из команды C, которые путешествуют.')
print()
for i in players_dict:
  if players_dict[i].get('status') == 'Travel' and players_dict[i].get(
      'team') == 'C':
    print(players_dict[i].get('name'))