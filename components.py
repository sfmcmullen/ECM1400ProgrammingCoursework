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

    return board


if __name__ == '__main__':
    g.single_game_loop()
    