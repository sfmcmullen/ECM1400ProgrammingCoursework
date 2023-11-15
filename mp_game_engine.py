"""Contains ai game functions"""
import components as c

#Dictionary of players. Key = Username, Value = Board
players = {}
#Stores the values of previous attacks for generate_attack
ai_previous_attacks = []


def cli_coordinates_input():
    """Takes inputs for x, y cooridnates and returns tuple."""

    row = int(input("What is the row you would like to attack? >>>"))
    column = int(input("What is the column you would like to attack? >>>"))
    return (row, column)


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


def generate_attack(board_size = 10):
    """Returns a tuple with coordinates to be passed to the attack function"""
    import random as r

    row, column = r.randint(0, board_size - 1), r.randint(0, board_size - 1)
    while (row, column) in ai_previous_attacks:
        row, column = r.randint(0, board_size - 1), r.randint(0, board_size - 1)

    ai_previous_attacks.append((row, column))
    return (row, column)


def ai_opponent_game_loop():
    """Runs a single loop of the game against ai"""

    print("~~~~~ Welcome to Battleships! ~~~~~")

    #Creates battleships for both players
    battleships = {}
    battleships['player1'] = c.create_battleships()
    battleships['player2'] = c.create_battleships()

    #creates a board and battleships and then places the batttleships and stores in p1
    players['player1'] = c.place_battleships(c.initialise_board(), battleships['player1'], 'Custom')
    #creates a board and battleships and then places the batttleships and stores in p2
    players['player2'] = c.place_battleships(c.initialise_board(), battleships['player2'], 'Random')

    while True:
        #User attack
        coordinates = cli_coordinates_input()
        result = {True: "hit", False: "missed"}
        print(f"You {result[attack(coordinates, players['player2'], battleships['player2'])]} the AI.")
        #AI attack
        coordinates = generate_attack()
        result = {True: "hit", False: "Miss"}
        print(f"The AI {result[attack(coordinates, players['player1'], battleships['player1'])]} you.")

        print("\nUser's Board")
        display_board(players['player1'])
        print("\nAI's Board")
        display_board(players['player2']) #Used during testing to see the effect on AI's board
        print("")

        #Used to check if there exists a ship longer than 0 (not sunk) for both players
        if not(any(x != 0 for x in battleships['player1'].values())):
            print("~~~~~~ Good attempt. Better luck next time! ~~~~~~")
            break
        if not(any(x != 0 for x in battleships['player2'].values())):
            print("~~~~~~ Congrats! You beat the AI ~~~~~~")
            break


def display_board(board):
    """Displays an ASCII representation of the input board"""
    symbols = {'Aircraft Carrier': 'A','Battleship': 'B', 'Cruiser': 'C', 'Submarine': 'S', 'Destroyer': 'D', None: '_'}

    row_num = 0
    print("   0 1 2 3 4 5 6 7 8 9")
    print("   ___________________")
    for row in board:
        row_ascii = ""
        for column in row:
            row_ascii += (f"{symbols[column]}|")
        print(f"{row_num} |{row_ascii}")
        row_num += 1
    
    print("KEY:\nAircraft Carrier: A, Battleship: B, Cruiser: C, Submarine: S, Destroyer: D")