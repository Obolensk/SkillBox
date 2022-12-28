# TODO здесь писать код

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
    if max_deep >= deep:
      return
    if isinstance(i, dict):
      res = find(i, key)
      if res:
        break
  else:
    res = None
  return res

my_key = input('Искомый ключ: ')
deep = 0
for keys in site:
  if my_key == keys:
    break
  else:
    if my_key in site[keys]:
      deep += 1

# print(deep)
ask_deep = input('Хотите ввести максимальную глубину? Y/N: ')
if ask_deep == 'n':
  max_deep = 0
elif ask_deep == 'y':
  max_deep = int(input('Введите максимальную глубину: '))
value = find(site, my_key)
if value:
  print(value)
else:
  print('Такого ключа нет в словаре')
