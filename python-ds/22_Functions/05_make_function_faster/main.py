# def calculating_math_func(data):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     result /= data ** 3
#     result = result ** 10
#     return result

# TODO оптимизировать функцию




def calculating_math_func(data):
    result = 1
    for index in range(1, data + 1):
        result *= index
        print()
        print('result *= index = ', result)
        print()
    result /= data ** 3
    print('result /= data ** 3 = ', result)
    result = result ** 10
    print('result = result ** 10 = ', result)
    return result

print(calculating_math_func(5))
