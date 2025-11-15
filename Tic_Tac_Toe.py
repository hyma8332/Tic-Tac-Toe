from random import randrange

# -------------------------------
# Function to display the board
# -------------------------------
def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|   " + str(row[0]) + "   |   " + str(row[1]) + "   |   " + str(row[2]) + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# -------------------------------
# Check if someone has won
# -------------------------------
def victory_for(board, sign):
    # Rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == sign:
            return True

    # Columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == sign:
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True

    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False

# -------------------------------
# Check if a square is free
# -------------------------------
def make_list_of_free_fields(board):
    free = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free.append((r, c))
    return free

# -------------------------------
# User move
# -------------------------------
def enter_move(board):
    free = make_list_of_free_fields(board)
    while True:
        move = input("Enter your move: ")
        if not move.isdigit():
            print("Invalid input. Enter a number 1–9.")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("Out of range. Try again.")
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if (row, col) in free:
            board[row][col] = 'O'
            break
        else:
            print("Square already taken. Try again.")

# -------------------------------
# Computer move (random)
# -------------------------------
def draw_move(board):
    free = make_list_of_free_fields(board)
    idx = randrange(len(free))
    row, col = free[idx]
    board[row][col] = 'X'

# -------------------------------
# MAIN PROGRAM
# -------------------------------
board = [
    [1, 2, 3],
    [4, 'X', 6],  # Computer starts with X in the center
    [7, 8, 9]
]

while True:
    display_board(board)

    # User move
    enter_move(board)

    display_board(board)

    # Check if user wins
    if victory_for(board, 'O'):
        print("You have won!")
        break

    # Check for tie after user move
    if len(make_list_of_free_fields(board)) == 0:
        print("It's a tie!")
        break

    # Computer move
    draw_move(board)

    # Check for tie after computer move
    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("It's a tie!")
        break

    # Check if computer wins
    if victory_for(board, 'X'):
        display_board(board)
        print("Computer wins!")
        break

