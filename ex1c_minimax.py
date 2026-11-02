"""Ex 1c - Minimax (Tic-Tac-Toe). AI = X, Human = O"""
PLAYER_X, PLAYER_O, EMPTY = 1, -1, 0

def evaluate(board):
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != EMPTY:
            return board[r][0]
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != EMPTY:
            return board[0][c]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return 0

def is_moves_left(board):
    return any(cell == EMPTY for row in board for cell in row)

def minimax(board, is_max):
    score = evaluate(board)
    if score != 0:
        return score
    if not is_moves_left(board):
        return 0
    best = -float('inf') if is_max else float('inf')
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                board[r][c] = PLAYER_X if is_max else PLAYER_O
                val = minimax(board, not is_max)
                board[r][c] = EMPTY
                best = max(best, val) if is_max else min(best, val)
    return best

def find_best_move(board):
    best_val, best_move = -float('inf'), (-1, -1)
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                board[r][c] = PLAYER_X
                val = minimax(board, False)
                board[r][c] = EMPTY
                if val > best_val:
                    best_move, best_val = (r, c), val
    return best_move

def print_board(board):
    for row in board:
        print(" ".join("X" if x == PLAYER_X else "O" if x == PLAYER_O else "." for x in row))

# X has a winning move at (2,0) (anti-diagonal)
board = [
    [PLAYER_X, PLAYER_O, PLAYER_X],
    [PLAYER_O, PLAYER_X, EMPTY],
    [EMPTY,    PLAYER_O, PLAYER_O],
]
print("Current Board:")
print_board(board)
move = find_best_move(board)
print(f"\nBest Move: {move}")
board[move[0]][move[1]] = PLAYER_X
print("\nBoard after best move:")
print_board(board)

"""
OUTPUT:
Current Board:
X O X
O X .
. O O

Best Move: (2, 0)

Board after best move:
X O X
O X .
X O O
"""
