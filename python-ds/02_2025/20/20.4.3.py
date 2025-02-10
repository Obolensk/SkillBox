my_string = ' ab1n32kz2'
nums = ''

for sym in my_string:
    if sym.isdigit():
        nums += sym

new_nums = sorted(set(nums))

nums = ''
for i in sorted(set(new_nums)):
    nums += i

print(nums)

