"""Ex 1a - N-Queens using Backtracking (with timing for 4x4, 8x8, 10x10)"""
import time

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j]:
            return False
    return True

def solve(board, row, n, solutions):
    if row == n:
        solutions.append([r[:] for r in board])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n, solutions)
            board[row][col] = 0

def print_board(board):
    for row in board:
        print(" ".join("Q" if c else "." for c in row))
    print()

def n_queens(n):
    solutions = []
    solve([[0] * n for _ in range(n)], 0, n, solutions)
    return solutions

if __name__ == "__main__":
    sols = n_queens(8)
    print("First 2 solutions for 8x8:\n")
    for s in sols[:2]:
        print_board(s)
    print(f"Total solutions for 8x8: {len(sols)}\n")

    print("Performance analysis")
    print(f"{'N':<5}{'Solutions':<12}{'Time (s)':<10}")
    for n in (4, 8, 10):
        t = time.time()
        count = len(n_queens(n))
        print(f"{n:<5}{count:<12}{time.time() - t:<10.4f}")

"""
OUTPUT:
First 2 solutions for 8x8:

Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .

Q . . . . . . .
. . . . . Q . .
. . . . . . . Q
. . Q . . . . .
. . . . . . Q .
. . . Q . . . .
. Q . . . . . .
. . . . Q . . .

Total solutions for 8x8: 92

Performance analysis
N    Solutions   Time (s)  
4    2           0.0000    
8    92          0.0047    
10   724         0.1044    
"""
