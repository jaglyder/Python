#==========================================================================
# PROGRAM PURPOSE:... Ch5 D3
# AUTHOR:............ Glyder, Jillian
# COURSE:............ CSC 131-002
# TERM:.............. Fall 2019
# COLLABORATION:..... 
# WORK TIME(h:mm):... 2:00
#==========================================================================
# Arrays for the coordinates entered by each player in chronological order
playerO_coordinates = []
playerX_coordinates = []

# Arrays for tracking the status of each coordinate (0 = player 1 (O), 1 = player 2 (X), and 3 = not taken)
row_coordinates = [[3,3,3],[3,3,3],[3,3,3]]
col_coordinates = [[3,3,3],[3,3,3],[3,3,3]]
diag_coordinates = [[3,3,3],[3,3,3]]

# 0 will represent player 1 (O player), and 1 will represent player 2 (X player)
current_player = 0

# Method for retreiving the current player's move:
def player_move():
    player = ""
    if current_player == 0:
        player = "Player 1 (O)"
    else:
        player = "Player 2 (X)"
    x_coord = input(player + ": Enter the Column coordinate for your move: ")
    y_coord = input(player + ": Enter the Row coordinate for your move: ")
    if (x_coord != "0") and (x_coord != "1") and (x_coord != "2"):
        return [0]
    if (y_coord != "0") and (y_coord != "1") and (y_coord != "2"):
        return [0]
    coordinate = [int(x_coord), int(y_coord)]
    for x in playerO_coordinates:
        if coordinate == x:
            return [0]
    for x in playerX_coordinates:
        if coordinate == x:
            return [0]
    return coordinate


print("The game is Tic Tac Toe. The first player to go will be O (second player being X), \nand the prompt will alternate back and forth between players until one player gets \nthree in a row. The prompt will ask for a row coordinate and a column coordinate \nbetween 0, 1 and 2.")
print("The board coordinates are as follows: ")
print("")
print("  0  1  2")
print("0 -  -  -")
print("1 -  -  -")
print("2 -  -  -")
print("")
game_continue = True
while game_continue:
    # First step: getting coordinates via player_move() and making sure the player doesnt enter an invalid input
    coordinate = []
    works = True
    while works:
        coordinate = player_move()
        if coordinate == [0]:
            print("****You either entered a coordinate that has already been taken, or you gave an invalid input. Try again! (only enter integers 0..2)****")
            works = True
            continue
        works = False

    # Adding the cooridnates to playerX_coordinates, playerO_coordinates, col_coordinates, row_coordinates, diag_coordinates
    if current_player == 1:
        playerX_coordinates.append(coordinate)
        col_coordinates[coordinate[0]][coordinate[1]] = 1
        row_coordinates[coordinate[1]][coordinate[0]] = 1
        if (coordinate[0] == 0) and (coordinate[1] == 0):
            diag_coordinates[0][0] = 1
        elif (coordinate[0] == 1) and (coordinate[1] == 1):
            diag_coordinates[0][1] = 1
            diag_coordinates[1][1] = 1
        elif (coordinate[0] == 2) and (coordinate[1] == 2):
            diag_coordinates[0][2] = 1
        elif (coordinate[0] == 2) and (coordinate[1] == 0):
            diag_coordinates[1][0] = 1
        elif (coordinate[0] == 0) and (coordinate[1] == 2):
            diag_coordinates[1][2] = 1

    if current_player == 0:
        playerO_coordinates.append(coordinate)
        col_coordinates[coordinate[0]][coordinate[1]] = 0
        row_coordinates[coordinate[1]][coordinate[0]] = 0
        if (coordinate[0] == 0) and (coordinate[1] == 0):
            diag_coordinates[0][0] = 0
        elif (coordinate[0] == 1) and (coordinate[1] == 1):
            diag_coordinates[0][1] = 0
            diag_coordinates[1][1] = 0
        elif (coordinate[0] == 2) and (coordinate[1] == 2):
            diag_coordinates[0][2] = 0
        elif (coordinate[0] == 2) and (coordinate[1] == 0):
            diag_coordinates[1][0] = 0
        elif (coordinate[0] == 0) and (coordinate[1] == 2):
            diag_coordinates[1][2] = 0


    # Print the current tictactoe board
    print("")
    for x in row_coordinates:
        string1 = ""
        if x[0] == 3:
            string1 = string1 + "- "
        elif x[0] == 0:
            string1 = string1 + "O "
        elif x[0] == 1:
            string1 = string1 + "X "

        if x[1] == 3:
            string1 = string1 + "- "
        elif x[1] == 0:
            string1 = string1 + "O "
        elif x[1] == 1:
            string1 = string1 + "X "

        if x[2] == 3:
            string1 = string1 + "- "
        elif x[2] == 0:
            string1 = string1 + "O "
        elif x[2] == 1:
            string1 = string1 + "X "
        print(string1)
    print("")

    # Checking each row column and  to see if there is a winner or a tie before moving on to the next iteration of the loop
    break_var = False
    player = ""
    if current_player == 0:
        player = "Player 1 (O)"
    else:
        player = "Player 2 (X)"
    for x in row_coordinates:
        if (x[0]==current_player) and (x[1]==current_player) and (x[2]==current_player):
            print("Congratulations " + player + ", you've won the game! (restart the program to play again)")
            game_continue = False
            break_var = True

    for x in col_coordinates:
        if (x[0]==current_player) and (x[1]==current_player) and (x[2]==current_player):
            print("Congratulations " + player + ", you've won the game! (restart the program to play again)")
            game_continue == False
            break_var = True

    for x in diag_coordinates:
        if (x[0]==current_player) and (x[1]==current_player) and (x[2]==current_player):
            print("Congratulations " + player + ", you've won the game! (restart the program to play again)")
            game_continue = False
            break_var = True

    if ((len(playerO_coordinates) + len(playerX_coordinates)) == 9) and (break_var == False):
        print("Game has resulted in a Tie, Neither player wins! (restart the program to play again)")
        game_continue = False
        break_var = True

    if current_player == 0:
        current_player = 1
    elif current_player == 1:
        current_player = 0

    if break_var:
        break
