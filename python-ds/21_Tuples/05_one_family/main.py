# TODO здесь писать код

my_dict = {
  'Иванова Иван': 15,
  'Иванова Аня': 16,
  'Сидоров Никита': 35,
  'Сидорова Алина': 34,
  'Сидоров Павел': 10
}

surname = input('Введите фамилию: ')

for name in my_dict:
  if surname.lower() in name.lower():
    print(name, my_dict[name])
