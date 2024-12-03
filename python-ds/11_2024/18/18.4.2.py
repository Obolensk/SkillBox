
nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]

print('1.', end=' ')
print(nums[0:5])

print('2.', end=' ')
print(nums[0:-2])

print('3.', end=' ')
print([nums[i] for i in range(len(nums)) if i % 2 == 0])

print('4.', end=' ')
print([nums[i] for i in range(len(nums)) if i % 2 != 0])

print('5.', end=' ')
rev_num = [nums[len(nums) - 1 - i] for i in range(len(nums))]
print(rev_num)

print('6.', end=' ')
print([rev_num[i] for i in range(len(nums)) if i % 2 == 0])
