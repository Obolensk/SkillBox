
price_list = [float(input('Цена на товар: ')) for i in range(5)]

x = float(input('Повышение на первый год: '))
y = float(input('Повышение на второй год: '))

first_year_prices = [i * (1 + x / 100) for i in price_list]
second_year_prices = [i * (1 + y / 100) for i in first_year_prices]

print('Сумма цен за каждый год:', round(sum(price_list), 2), round(sum(first_year_prices), 2), round(sum(second_year_prices), 2))