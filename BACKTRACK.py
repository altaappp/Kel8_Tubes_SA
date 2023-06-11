import random
import time

# The Tic-Tac-Toe board
board = ['-'] * 9
player = 'X'
computer = 'O'

# Function to print the board
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], board[i+1], board[i+2])

# Function to check if a player has won
def check_win(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return '-' not in board

# Function to evaluate the board for the backtracking strategy
def evaluate_board(board):
    if check_win(board, computer):
        return 1
    elif check_win(board, player):
        return -1
    else:
        return 0

# Backtracking algorithm
def backtracking(board, depth, maximizing_player):
    if check_win(board, computer):
        return 1
    elif check_win(board, player):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = computer
                eval = backtracking(board, depth + 1, False)
                board[i] = '-'
                max_eval = max(max_eval, eval)
                if max_eval == 1:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = player
                eval = backtracking(board, depth + 1, True)
                board[i] = '-'
                min_eval = min(min_eval, eval)
                if min_eval == -1:
                    break
        return min_eval

# Function to make a move using the backtracking strategy
def make_move(board):
    best_eval = float('-inf')
    best_move = None
    for i in range(9):
        if board[i] == '-':
            board[i] = computer
            eval = backtracking(board, 0, False)
            board[i] = '-'
            if eval > best_eval:
                best_eval = eval
                best_move = i
            if best_eval == 1:
                break
    board[best_move] = computer

# Main game loop
def play_game():
    while True:
        print_board(board)
        print("\n")

        # Player X's turn
        print("Player X's turn:")
        move = random.choice([i for i, val in enumerate(board) if val == '-'])
        board[move] = player
        if check_win(board, player):
            print_board(board)
            print("X wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print_board(board)
        print("\n")

        # Player O's turn
        print("Player O's turn:")
        make_move(board)
        if check_win(board, computer):
            print_board(board)
            print("O wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

start = time.time()
play_game()
end = time.time()
print("The game finished in:", end - start, "seconds")
