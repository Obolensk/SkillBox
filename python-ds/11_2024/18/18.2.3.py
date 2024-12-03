price_list = [float(input('Цена на товар: ')) for _ in range(5)]
# print(price_list)
first_year = int(input('Повышение на первый год: '))
second_year = int(input('Повышение на второй год: '))

first_price = [i * (1 + first_year/100) for i in price_list]
second_price = [i * (1 + second_year/100) for i in first_price]

# prices_summ = [sum(price_list), sum(first_price), sum(second_price)]
print('Сумма цен за каждый год:', round(sum(price_list), 2), round(sum(first_price), 2), round(sum(second_price), 2))