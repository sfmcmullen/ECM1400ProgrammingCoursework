"""Contains in-game functions"""
import components as c

def attack(coordinates, board, battleships):
    """Return true if the coordinate is a ship, else return false.
    If the ship value is 0 in battleships, then the ship is sunk."""

    if board[coordinates[0]][coordinates[1]] is not None:
        #Decrement the value of remaining pieces in the battleships dictionary
        battleships[board[coordinates[0]][coordinates[1]]] -= 1
        #Set the square to 0 as that area has been sunk
        board[coordinates[0]][coordinates[1]] = None
        return True

    return False


def cli_coordinates_input():
    """Takes inputs for x, y cooridnates and returns tuple."""

    x = int(input("What is the x-coordinate you would like to attack? >>>"))
    y = int(input("What is the y-coordinate you would like to attack? >>>"))
    return (x, y)


def single_game_loop():
    """Runs a single loop of the game."""

    print("~~~~~ Welcome to Battleships! ~~~~~")
    board = c.initialise_board() #create board
    battleships = c.create_battleships() #create ships
    board = c.place_battleships(board, battleships) #add ships to board

    non_zero_exists = True
    while non_zero_exists:

        coordinates = cli_coordinates_input()
        result = {True: "Hit", False: "Miss"}
        print(result[attack(coordinates, board, battleships)])
        print("Current Board: ") #FOR TESTING. REMOVE LATER!!!!!!!!!!!!!!
        print(board)
        print("")

        #Used to check if there exists a ship longer than 0 (not sunk)
        for value in battleships.values():
            if value != 0:
                non_zero_exists = True
                break
            non_zero_exists = False

    print("~~~~~ Game Over ! ~~~~~")
