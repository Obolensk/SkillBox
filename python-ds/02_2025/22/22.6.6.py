
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам iPhone недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

print(site)


def new_site(phone):
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

new_site('SAMSUNG')

site_num = int(input('Сколько будет сайтов? '))

for sites in range(site_num):
    new_phone = input('Введите название продукта для нового сайта: ')
    new_site(new_phone)


