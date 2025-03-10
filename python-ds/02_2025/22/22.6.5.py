#
# def calculating_math_func(data):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     result /= data ** 3
#     result = result ** 10
#     return result
#
# print(calculating_math_func(30))

#
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


def new_func(data):
    return (factorial(data) / data ** 3) ** 10

print(new_func(30))

