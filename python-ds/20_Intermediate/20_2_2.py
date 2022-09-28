incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

print()
print('Общий доход за год составил {0} рублей'.format(sum(incomes.values())))
print()
min_fruit = ''
for keys in incomes:
    if incomes[keys] == min(incomes.values()):
        min_fruit = keys
print('Самый маленький доход у {0}. Он составляет {1} рублей'.format(min_fruit, min(incomes.values())))
incomes.pop(min_fruit)
print('Итоговый словарь: {0}'.format(incomes))