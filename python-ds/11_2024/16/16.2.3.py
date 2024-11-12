dogs = int(input('Введите количество собак: '))
score_list = []
new_score_list = []
max_i = 0
min_i = 0

for i in range(1, dogs + 1):
    print('Введите очки собаки №', i, end=' ')
    score = int(input())
    score_list.append(score)

print(score_list)

print(min(score_list))
print(max(score_list))

for i in range(len(score_list)):
    if score_list[i] == min(score_list):
        min_i = i
    elif score_list[i] == max(score_list):
        max_i = i

print()
print('min_i = ', min_i)
print('max_i = ', max_i)
new_score_list = list(score_list)
print('new_score_list = ', new_score_list)

new_score_list[min_i] = max(score_list)
print('new_score_list = ', new_score_list)

new_score_list[max_i] = min(score_list)

print('new_score_list = ', new_score_list)