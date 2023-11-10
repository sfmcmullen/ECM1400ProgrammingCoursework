'''Module containing functions to setup componenets of the game.'''
import game_engine as g

def initialise_board(size = 10):
    """Returns a list of 'size' elements, with each 
    element beign a list containing 'size' elements."""

    #return [[None] * size] * size
    board = []

    for i in range(10):
        board.append([None] * 10)

    return board


def create_battleships(filename = 'battleships.txt'):
    """Reads the file and returns a dictionary containing 
    keys as battleship name and value as its size."""

    battleships = {}

    f = open(filename, 'r')
    for line in f:
        battleships[line.split('-')[0]] = int(line.replace('\n', '').split('-')[1])

    return battleships


def place_battleships(board, ships, algorithm = 'Simple'):
    """Places the battleships on the board using the 
    specified algorithm and returns the board."""
    if algorithm == 'Simple':
        row = 0
        for ship in ships:
            for col in range(ships[ship]):
                board[row][col] = ship
            row += 1

    if algorithm == 'Random':
        import random as r

        for ship in ships:
            #Chooses wether the ship will be horiaontal or vertical
            rotation = r.choice(['Horizontal', 'Vertical'])
            print(rotation)

            if rotation == 'Horizontal':
                while True:
                    row = r.randint(0, len(board) - 1)
                    col = r.randint(0, len(board) - ships[ship])
                    if all(x == None for x in board[row][col : (col + ships[ship])]):
                        break
                for i in range(ships[ship]):
                    board[row][col + i] = ship

            if rotation == 'Vertical':
                while True:
                    row = r.randint(0, len(board) - ships[ship])
                    col = r.randint(0, len(board) - 1)

                    if all(x == None for x in board[row][col : col + (ships[ship])]):
                        break
                for i in range(ships[ship]):
                    board[row + i][col] = ship
                

    if algorithm == 'Custom':
        #Custom code
        print("Custom")

    return board


if __name__ == '__main__':

    g.single_game_loop()
    