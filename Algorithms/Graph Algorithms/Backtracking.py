# Backtracking example: N-Queens problem

def n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row, board):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                count += place_queens(n, row + 1, board)
        return count

    board = [-1] * n
    return place_queens(n, 0, board)

n = 4
print(n_queens(n))  # 2