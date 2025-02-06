from urllib.parse import ParseResult

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



print('Общий доход за год составил {:,} рублей'.format(sum(incomes.values())))

min_summ = min(incomes.values())

for item in incomes:
    if incomes[item] == min_summ:
        del_item = item

print('Самый маленький доход у {}. Он составляет {:,} рублей'.format(del_item, min_summ))

incomes.pop(del_item)
print('Итоговый словарь: {}'.format(incomes))
