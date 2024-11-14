
main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]

new_companies = [first_company, second_company, third_company]

# print(new_companies)

for comp in new_companies:
    main.extend(comp)
    # print(main)

print()
print(main)