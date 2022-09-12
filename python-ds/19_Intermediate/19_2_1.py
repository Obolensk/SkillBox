
name = input('Имя: ',)
order = input('Номер заказа: ', )

message = 'Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!'.format(
    name,
    order
)

print(message)