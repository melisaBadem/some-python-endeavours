from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))


print("Welcome to the Battleship Game! Guess where the battleship hides!\n")
print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Column: "))

    if guess_row == ship_row + 1 and guess_col == ship_col + 1:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
            print("Oops, that's not even in the ocean.")
        elif (board[guess_row - 1][guess_col - 1] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row - 1][guess_col - 1] = "X"

    print("\n")
    print_board(board)
    if turn == 3:
        print("Game Over")
        print("\nThe ship was on %d x %d" % (ship_row + 1, ship_col + 1))
        board[ship_row][ship_col] = "1"
        print_board(board)
    i = input("Press Enter to exit: ")
