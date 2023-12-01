"""Contains in-game functions"""
import components as c


def attack(coordinates, board, battleships):
    """Return true if the coordinate is a ship, else return false.
    If the ship value is 0 in battleships, then the ship is sunk."""
    
    if board[int(coordinates[0])][int(coordinates[1])] is not None:
        #Decrement the value of remaining pieces in the battleships dictionary
        battleships[board[int(coordinates[0])][int(coordinates[1])]] -= 1
        #Set the square to 0 as that area has been sunk
        board[int(coordinates[0])][int(coordinates[1])] = None
        return True

    return False


def cli_coordinates_input():
    """Takes inputs for x, y coordinates and returns tuple."""

    y = int(input("What is the row you would like to attack? >>>"))
    x = int(input("What is the column you would like to attack? >>>"))
    return (y, x)


def simple_game_loop():
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
        print("")

        #Used to check if there exists a ship longer than 0 (not sunk)
        for value in battleships.values():
            if value != 0:
                non_zero_exists = True
                break
            non_zero_exists = False

    print("~~~~~ Game Over ! ~~~~~")
