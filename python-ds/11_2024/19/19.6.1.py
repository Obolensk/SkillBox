#
# Пример:
# Доступное меню: утиное филе;фланк-стейк;банановый пирог;плов
# На данный момент в меню есть: утиное филе, фланк-стейк, банановый пирог, плов


menu = 'утиное филе;фланк-стейк;банановый пирог;плов'

print(', '.join(menu.split(';')))