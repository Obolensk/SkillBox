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
print('html' in site)
print()

find_key = input('Введите искомый ключ: ')


def finder(struct, key):
    if key in struct:
        return struct[key]

    for keys in struct.values():
        if isinstance(keys, dict):
            return finder(keys, key)
        else:
            break




print(finder(site, find_key))