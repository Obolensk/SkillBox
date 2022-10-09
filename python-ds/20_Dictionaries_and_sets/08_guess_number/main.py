# TODO здесь писать код

import random

n = int(input('Введите максимальное число: '))
# print(nums)

ans = random.randint(1, n + 1)
print(ans)

answers = []
for i in range(1, n + 1):
  answers.append(i)
print(answers)


while True:
  nums = input('Нужное число есть среди вот этих чисел: ').split()
  if 'f' in nums:
    print('Артём мог загадать следующие числа:', answers)
    break
  elif str(ans) in nums:
    print('Ответ Артёма: Да')
    break
  else:
    for i in nums:
      if int(i) in answers:
        answers.remove(int(i))
      else:
        continue
    print('Ответ Артёма: Нет')
