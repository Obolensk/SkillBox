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


def find(str, key):
  if key in str:
    return str[key]

  for i in str.values():
    if isinstance(i, dict):
      res = find(i, key)
      if res:
        break
  else:
    res = None

  return res


my_key = input('Искомый ключ: ')
value = find(site, my_key)
if value:
  print(value)
else:
  print('Такого ключа нет в словаре')

