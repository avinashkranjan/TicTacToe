#initial imports
import time
# board
# display board
# play game
# handle game
# check win
# check rows
# check columns
# check diagonals
# check tie
# flip player


# --- Global Variables
# If game is still going
game_still_going = True

# Who won or Tie?
winner = None

# Who's Turn is it
current_player = "X"

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]


# Display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# defining a menu


# def menu():
    # Play Against another player
    # play against computer
    # Quit

# Display logo
def display_logo():
    print(
"""
$$$$$$$$\ $$\        $$$$$$$$\               $$$$$$$$\                  
\__$$  __|\__|       \__$$  __|              \__$$  __|                 
   $$ |   $$\  $$$$$$$\ $$ | $$$$$$\   $$$$$$$\ $$ | $$$$$$\   $$$$$$\  
   $$ |   $$ |$$  _____|$$ | \____$$\ $$  _____|$$ |$$  __$$\ $$  __$$\ 
   $$ |   $$ |$$ /      $$ | $$$$$$$ |$$ /      $$ |$$ /  $$ |$$$$$$$$ |
   $$ |   $$ |$$ |      $$ |$$  __$$ |$$ |      $$ |$$ |  $$ |$$   ____|
   $$ |   $$ |\$$$$$$$\ $$ |\$$$$$$$ |\$$$$$$$\ $$ |\$$$$$$  |\$$$$$$$\ 
   \__|   \__| \_______|\__| \_______| \_______|\__| \______/  \_______|
                                                                                                                                     
"""
)

#greet the users

#defining some functions
def greet_users():
    time.sleep(1)
    print("Welcome to tic-tac-toe game , pls note that there must be two players")
    time.sleep(2)
    print("Please wait...")




greet_users()
USER_X_NAME = str(input("What is the name of user X ? ")).title()
USER_O_NAME = str(input("What is the name of user O ? ")).title()

print("processing, pls wait ")
time.sleep(1)
print(f"USER X : {USER_X_NAME}")
print(f"USER O : {USER_O_NAME}")
is_x_ready = str(input(f"Is {USER_X_NAME} ready to start the game ? Type X , if not ready type EXIT ").title())
if is_x_ready == "X":
    global is_o_ready
    is_o_ready = str(input(f"Is {USER_X_NAME} ready to start the game ? Type O , if not ready type EXIT ").title())
    if is_o_ready == "O":
        print("Ok so both of you are ready to play the game lets start")
    else:
        print(
            f"user {USER_O_NAME} is not ready to play the game is aborted, {USER_X_NAME} pls tell your friend to be "
            f"ready if you want to play the game , or find any other friend ;)")
else:
    print(f"user {USER_X_NAME} is not ready to play the game is aborted, {USER_O_NAME} pls tell your friend to be ready "
          f"if you want to play the game , or find any other friend ;)")

if is_o_ready == "O" and is_x_ready == "X":
    game_is_on = True

#giving the instructions

print("INSTRUCTIONS:\n 1. The boxes are designed serially,\n 2.like 1,2,3,\n         4,5,6,\n         7,8,9\n3. you have "
      "to type number where you want to put your mark")
print("---")
time.sleep(3)
print("I hope instructions are clear to both of the players , so lets start the same")
time.sleep(2)
print("Pls wait ")
time.sleep(3)

# Play a Game of Tic Tac Toe
def play_game():
    # Display the inital logo
    display_logo()
    # Display the inital board
    display_board()

    while game_still_going:

        # Handle a Single turn of an arbitary player
        handle_turn(current_player)
        # Check if game has ended
        check_if_game_over()
        # flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        if winner == "X":
            winner_name = USER_X_NAME
        else:
            winner_name = USER_O_NAME
        print("Booyah! " + winner_name + " Won.")
    elif winner == None:
        print("And Tie It is.")


# Handle a Single Turn of an arbitarary player
def handle_turn(player):
    position = input(
        "[" + player + "'s Turn] Choose a Position from 1-9: ")

    valid = False

    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input(
                "Invalid Position, Please Try Again.\n" "[" + player + "'s Turn] Choose a Position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there.")
            display_board()

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # set up global winner
    global winner
    # check Rows
    row_winner = check_rows()
    # check Columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    # set up global variable
    global game_still_going

    # check if any of the rows have all the same values (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row there's a match, flag that there's win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return


def check_columns():
    # set up global variable
    global game_still_going

    # check if any of the columns have all the same values (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column there's a match, flag that there's win
    if column_1 or column_2 or column_3:
        game_still_going = False

        # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return


def check_diagonals():
    # set up global variable
    global game_still_going

    # check if any of the diagonals have all the same values (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If any diagonal there's a match, flag that there's win
    if diagonal_1 or diagonal_2:
        game_still_going = False

        # Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    return


def check_if_tie():
    # Set up global Varible
    global game_still_going
    # Check if there's Tie
    if "-" not in board:
        game_still_going = False

    return


def flip_player():
    # Set up global Varible
    global current_player
    # If Current player is X change it to O and Vice-Versa
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return


play_game()
