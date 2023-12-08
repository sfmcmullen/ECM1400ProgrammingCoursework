from components import initialise_board, create_battleships, place_battleships
from game_engine import attack


def test_initialise_board_return_size():
    """
    Test if the initialise_board function returns a list of the correct size.
    """
    size = 10
    # Run the function
    board = initialise_board(size)
    # Check that the return is a list
    assert isinstance(board, list), "initialise_board function does not return a list"
    # check that the length of the list is the same as board
    assert len(board) == size, "initialise_board function does not return a list of the correct size"
    for row in board:
        # Check that each sub element is a list
        assert isinstance(row, list), "initialise_board function does not return a list of lists"
        # Check that each sub list is the same size as board
        assert len(row) == size, "initialise_board function does not return lists of the correct size"


def test_create_battleships_return_values():
    """
    Test if the create_battleships function reads from the batlleships.txt file 
    and returns a dictionary in the correct format of Ship:Size containing these values.
    """
    filename = "battleships.txt"
    # Run the function
    ships = create_battleships(filename)
    # Check that the return is a dictionary
    assert isinstance(ships, dict), "create_battleships function does not return a list."
    # Check that each key-value pair are strings
    for ship in ships:
        # Check key is a string
        assert isinstance(ship, str), "create_ships function does not return a dictionary with strings as its keys."
        # Check value is a string
        assert isinstance(ships[ship], int), "create_battleships function doesn't return a dictionary with integers as its values"


def test_place_battleships_simple_algorithm():
    """
    Test if the place_battleships function uses the correct (simple) algorithm when placing 
    battleships and the expected outcome is returned.
    """
    algorithm = 'Simple'
    #Create an empty board of size 10
    empty_board = [
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None]]
    #Create a board filled with the expected outcome of using the simple algorithm
    simple_board = [
             ['Aircraft_Carrier', 'Aircraft_Carrier', 'Aircraft_Carrier', 'Aircraft_Carrier', 'Aircraft_Carrier', None, None, None, None, None],
             ['Battleship', 'Battleship', 'Battleship', 'Battleship', None, None, None, None, None, None],
             ['Cruiser', 'Cruiser', 'Cruiser', None, None, None, None, None, None, None],
             ['Submarine', 'Submarine', 'Submarine', None, None, None, None, None, None, None],
             ['Destroyer', 'Destroyer', None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None]]
    #Create the ships to be placed on the board
    ships = {
        'Aircraft_Carrier': 5,
        'Battleship': 4,
        'Cruiser': 3,
        'Submarine': 3,
        'Destroyer': 2
    }
    #Run the function and store the output into a test board
    test_board = place_battleships(empty_board, ships, algorithm)
    #Check that the board returned by the function is equal to the expected output
    assert test_board == simple_board, "create_battleships does not place ships in a simple algorithm format"


def test_attack_function():
    """
    Test if the attack function returns the correct Boolean when 
    identifying if a square contains a ship.
    """
    # Use a 2x2 grid to test if the function can idenotfy hits or misses
    board = [
        [None, 'Ship1'],
        ['Ship2', 'Ship2']
    ]
    # Create a temporary battleships dictionary to see if the values are changed when an attack happens
    battleships = {
        'Ship1': 1,
        'Ship2': 2
    }

    # Test (0, 0) is a miss
    assert attack((0, 0), board, battleships) == False, "The attack function didn't coorectly identify a miss."
    assert battleships['Ship1'] == 1, "The attack function didn't subtract from the correct ship value in the battleship dictionary."
    assert battleships['Ship2'] == 2, "The attack function didn't subtract from the correct ship value in the battleship dictionary."
    # Test (0, 1) is a hit on Ship1
    assert attack((0, 1), board, battleships) == True, "The attack function didn't coorectly identify a miss."
    assert battleships['Ship1'] == 0, "The attack function didn't subtract from the correct ship value in the battleship dictionary."
    assert battleships['Ship2'] == 2, "The attack function didn't subtract from the correct ship value in the battleship dictionary."
    # Test (1, 0) is a hit on Ship2
    assert attack((1, 0), board, battleships) == True, "The attack function didn't coorectly identify a miss."
    assert battleships['Ship1'] == 0, "The attack function didn't subtract from the correct ship value in the battleship dictionary."
    assert battleships['Ship2'] == 1, "The attack function didn't subtract from the correct ship value in the battleship dictionary."
    # Test (1, 1) is a hit on Ship2
    assert attack((1, 1), board, battleships) == True, "The attack function didn't coorectly identify a miss."
    assert battleships['Ship1'] == 0, "The attack function didn't subtract from the correct ship value in the battleship dictionary."
    assert battleships['Ship2'] == 0, "The attack function didn't subtract from the correct ship value in the battleship dictionary."
