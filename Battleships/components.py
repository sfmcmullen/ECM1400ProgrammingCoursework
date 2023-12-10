'''Module containing functions to setup components of the game.'''
import game_engine as g
import mp_game_engine as mg
import random as r
import json

def initialise_board(size = 10):
    """Returns a list of 'size' elements, with each 
    element being a list containing 'size' elements."""
    board = []

    for _ in range(10):
        board.append([None] * 10)

    return board


def create_battleships(filename = 'battleships.txt'):
    """Reads the file 'filename' and returns a dictionary containing 
    keys as battleship name and value as its size."""

    battleships = {}

    # Loop through each line of the file and split it into the part before and after ':'
    f = open('Battleships/' + filename, 'r')
    for line in f:
        battleships[line.split(':')[0]] = int(line.replace('\n', '').split(':')[1])

    return battleships


def place_battleships(board, ships, algorithm = 'Simple'):
    """Places the battleships on the board using the 
    specified algorithm and returns the board."""

    # Board is accessed where each list is a row and then 
    # each item in the list is a column in that row

    if algorithm == 'Simple':
        row = 0
        for ship in ships:
            for col in range(ships[ship]):
                board[row][col] = ship
            row += 1

    if algorithm == 'Random':
        for ship in ships:
            # Chooses wether the ship will be horiaontal or vertical
            rotation = r.choice(['Horizontal', 'Vertical'])

            if rotation == 'Horizontal':
                while True:
                    row = r.randint(0, len(board) - 1)
                    col = r.randint(0, len(board) - ships[ship])
                    if all(x == None for x in board[row][col : (col + ships[ship] + 1)]):
                        break
                for i in range(ships[ship]):
                    board[row][col + i] = ship

            if rotation == 'Vertical':
                while True:
                    row = r.randint(0, len(board) - ships[ship])
                    col = r.randint(0, len(board) - 1)

                    if all(board[row + x][col] == None for x in range(ships[ship])):
                        break
                for i in range(ships[ship]):
                    board[row + i][col] = ship
             

    if algorithm == 'Custom':
        f = open("Battleships/placement.json", "r")
        data = json.load(f)
        f.close()

        for ship in data:
            column = int(data[ship][0])
            row = int(data[ship][1])
            rotation = data[ship][2]

            if rotation == 'h':
                # Sets every position in row, from start col 
                # to the ships length elements away from that position horizontally
                for i in range(ships[ship]):
                    board[row][column + i] = ship
            else:
                # Sets every position in col, from start row 
                # to the ships length elements away from that position vertically
                for i in range(ships[ship]):
                    board[row + i][column] = ship

    return board


if __name__ == '__main__':

    # Runs a simple game against computer made board,
    # but just attacking with no computer return fire
    g.simple_game_loop()

    # Runs a game against a random computer board and custom user board,
    # with the computer also returning fire against the users board
    mg.ai_opponent_game_loop()
