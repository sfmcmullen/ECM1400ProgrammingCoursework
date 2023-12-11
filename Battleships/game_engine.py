"""Contains in-game functions"""
import components as c


def attack(coordinates, board, battleships):
    """Return true if the coordinate (row,col) is a ship, else return false.
    If the ship value is 0 in battleships, then the ship is sunk."""
    try:
        if board[int(coordinates[0])][int(coordinates[1])] is not None:
            #Decrement the value of remaining pieces in the battleships dictionary
            battleships[board[int(coordinates[0])][int(coordinates[1])]] -= 1
            #Set the square to 0 as that area has been sunk
            board[int(coordinates[0])][int(coordinates[1])] = None
            return True
    except Exception as exc:
        print(f"An error was encountered:\n{exc}\n")

    return False


def cli_coordinates_input():
    """Takes inputs for x, y coordinates and returns tuple."""
    while True:
        try:
            y = int(input("What is the row you would like to attack? >>>"))
            x = int(input("What is the column you would like to attack? >>>"))
            break
        except TypeError as exc:
            print(f"Incorrect value type entered:\n{exc}\n")
            #raise TypeError("Incorrect value type entered.") from exc
        except ValueError as exc:
            print(f"Incorrect value entered:\n{exc}\n")
            #raise ValueError("Incorrect value entered.") from exc
        except Exception as exc:
            print(f"An error was encountered:\n{exc}\n")
            #raise Exception("An error was encountered.") from exc

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
