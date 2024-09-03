# Tic-Tac-Toe game in Python

# Function to print the board
def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check for a win
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
                      (0, 4, 8), (2, 4, 6)]            # Diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Function to check for a draw
def check_draw(board):
    return all(spot != " " for spot in board)

# Main game function
def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != " ":
                print("This spot is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

# Start the game
tic_tac_toe()
