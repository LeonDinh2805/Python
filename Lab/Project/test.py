# Initialize the Tic Tac Toe board as a 3x3 list
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if a player has won
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Main game loop
current_player = 'X'
while True:
    display_board(board)
    print(f"Player {current_player}'s turn")
    
    # Get the row and column from the current player
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Update the board with the player's move
    board[row][col] = current_player
    
    # Check if the current player has won
    if check_winner(board, current_player):
        display_board(board)
        print(f"Player {current_player} wins!")
        break
    
    # Check if the board is full (tie)
    if is_board_full(board):
        display_board(board)
        print("It's a tie!")
        break
    
    # Switch to the other player for the next turn
    current_player = 'X' if current_player == 'O' else 'O'
