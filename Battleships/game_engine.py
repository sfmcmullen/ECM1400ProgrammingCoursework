"""
Module containing the functions used to carry out a request for user's
attack coordinates and then an attack involving the request coordinates.
Simple game loop then utilises these functions to carry out a game against
a simple board.
"""

import components as c


def attack(coordinates, board, battleships):
    """
    Take the coordinates (row,col) to attack and which board to complete
    the attack on as 2 parameters. The 3rd parameter battleships will update
    the value of the battleshiop that has been struck to be reduced in length
    by 1. It will return true if the coordinate is a ship, else return false.
    If the ship value is 0 in battleships, then the ship is sunk.
    """
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
    """
    Gets a user input via the terminal for a row and column to attack and
    then returns the value as a tuple (row, col)/(y, x).
    """
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
    """
    Runs a single loop of the game where the user will attack a simple
    generated board.
    """

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
