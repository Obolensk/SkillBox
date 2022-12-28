# site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам телефон недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на iphone',
#             'div': 'Купить',
#             'p': 'продать'
#         }
#     }
# }

# TODO здесь писать код


def site(phone):
  print()
  print('Сайт для {}'.format(phone))
  print()
  my_site = {
      'html': {
          'head': {
              'title': 'Куплю/продам {} недорого'.format(phone)
          },
          'body': {
              'h2': 'У нас самая низкая цена на {}'.format(phone),
              'div': 'Купить',
              'p': 'Продать'
          }
      }
  }
  print(my_site)

nums = int(input('Сколько сайтов: '))

for sites in range(nums):
  print()
  name = input('Введите название продукта для нового сайта: ')
  site(name)
