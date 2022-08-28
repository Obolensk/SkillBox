
import random

original_prices = [random.randint(-20, 20) for _ in range(5)]
print('original_prices = ', original_prices)

new_prc = original_prices[:]
total_loss = 0
for i in range(len(original_prices)):
    if new_prc[i] < 0:
        total_loss += new_prc[i]
        new_prc[i] = 0

print('new_prc = ', new_prc)
print('total_loss = ', total_loss)
