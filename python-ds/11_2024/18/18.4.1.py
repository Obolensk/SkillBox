import random


original_prices = [random.randint(-15, 15) for _ in range(5)]
# original_prices = [-12, 3, 5, -2, 1]
print(original_prices)
lostes = [i for i in original_prices if i < 0]

new_prices = original_prices[:]
for i in range(len(original_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0
print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))
print('Реальная сумма потерь составила', sum(lostes), 'руб.')

