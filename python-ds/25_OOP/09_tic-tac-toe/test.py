
board = [' ' for _ in range(9)]
row_ind = 3
row = board[row_ind * 3: (row_ind + 1) * 3]

print(board)
print(row_ind)
print(row)
print(6//3)

for i in range(9):
    print(i//3)