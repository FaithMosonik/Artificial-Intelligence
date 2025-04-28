import random
import time

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0: empty, 1: X, 2: O

def print_board(board):
    symbols = {0: ' ', 1: 'X', 2: 'O'}
    for i in range(3):
        row = [symbols[board[i*3 + j]] for j in range(3)]
        print("|".join(row))
        if i < 2:
            print("-----")
    print()  # Add space after printing the board

def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_draw(board):
    return 0 not in board

def minimax(board, is_maximizing):
    if check_win(board, 1):
        return 1
    elif check_win(board, 2):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = 1
                score = minimax(board, False)
                board[i] = 0
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = 2
                score = minimax(board, True)
                board[i] = 0
                best_score = min(score, best_score)
        return best_score

def find_best_move(board, is_maximizing):
    best_score = -float('inf') if is_maximizing else float('inf')
    best_move = -1
    for i in range(9):
        if board[i] == 0:
            board[i] = 1 if is_maximizing else 2
            score = minimax(board, not is_maximizing)
            board[i] = 0
            if (is_maximizing and score > best_score) or (not is_maximizing and score < best_score):
                best_score = score
                best_move = i
    return best_move

def get_random_move(board):
    """Returns a random empty cell."""
    empty_cells = [i for i in range(9) if board[i] == 0]
    return random.choice(empty_cells)

# Start the game
print("=== Tic-Tac-Toe Game ===")
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # Reset the board
current_player = 1  # Player 1 (X) starts

# Randomize the first move for Computer 1
first_move = get_random_move(board)
board[first_move] = 1
print(f"Computer 1 played:")
print_board(board)
current_player = 2

start = time.perf_counter()
while True:
    print(f"Computer {current_player}'s turn:")
    if current_player == 1:
        move = find_best_move(board, is_maximizing=True)
        board[move] = 1
    else:
        move = find_best_move(board, is_maximizing=False)
        board[move] = 2

    print(f"Computer {current_player} played:")
    print_board(board)

    if check_win(board, 1):
        print("Computer 1 (X) wins!")
        break
    if check_win(board, 2):
        print("Computer 2 (O) wins!")
        break
    if check_draw(board):
        print("It's a draw!")
        break

    current_player = 3 - current_player  # Switch players (1 -> 2, 2 -> 1)
    
end = time.perf_counter()
print(f"Code 1 Execution Time: {end - start:.6f} seconds")

