for row in range(5 + 1):
    print()
    for col in range(row, 12 + row):
        if row % 2 == 0:
            if col % 2 == 0:
                print(col, end='\t')
        else:
            if col % 2 != 0:
                print(col, end='\t')
