
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

print(site)

def find_key(key, dct):
    if key in dct:
        return dct[key]
    for value in dct.values():
        if isinstance(value, dict):
            res = find_key(key, value)
            if res:
                break
    else:
        res = None

    return res



my_key = input('Искомый ключ: ')

print('Значение {}'.format(find_key(my_key, site)))