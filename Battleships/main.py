"""
Module for the launching and running of the Flask web interface.
It creates an app route page where the attacks will take place and
also a placement page where the user will initlaise thier board.
The main game will then run in the back end here using the user's
web interface inputs.
"""

import os
import json
from flask import Flask, render_template, request
import components as c
import game_engine as g
import mp_game_engine as mg


# Checks to see if current environment is VSCODE.
# VSCode uses working directory: ...\ECM1400ProgrammingCoursework
# Others uses: ...\ECM1400ProgrammingCoursework\Battleships
# If environment in use is vscode then changes the cwd to be followed by \Battleships
try:
    environment = os.environ['TERM_PROGRAM']
    if environment == 'vscode':
        os.chdir(os.getcwd() + "\\Battleships")
except Exception as exc:
    pass


#Creates Flask app
app = Flask(__name__)

# Stores the ships in use this game.
# Not to be confused for the battleships dict that stores the individual player ship values.
ships = c.create_battleships()
# Dictionary of players. Key = Username, Value = Board
players = {}
# Stores the values of previous attacks for generate_attack
ai_previous_attacks = []
# Stores the battleships for the user and AI
battleships = {}
# Stores the size of the board in use
BOARD_SIZE = 10


@app.route('/placement', methods = ['GET', 'POST'])
def placement_interface():
    """
    Accepts a POST request containig the players board in the form of a config.json.
    Accepts a GET request which returns the placement.html template with a ships 
    dictionary and board size.
    """

    if request.method == 'GET':
        return render_template('placement.html', ships = ships, board_size = BOARD_SIZE)

    if request.method == 'POST':
        player_pieces = request.get_json()

        with open('placement.json', 'w', encoding = "utf-8") as file:
            json.dump(player_pieces, file)

        #Adds pieces to user board from placement.json
        players['player'] = c.place_battleships(players['player'], ships, 'Custom')
        #adds random pieces to AI board
        players['AI'] = c.place_battleships(players['AI'], ships, 'Random')

        return {"result": True}


@app.route('/', methods = ['GET'])
def root():
    """
    Returns the main.html template, passing a player board to the template.
    """
    return render_template('main.html', player_board = players['player'])


@app.route('/attack', methods = ['GET'])
def process_attack():
    """
    Accepts GET request contains two parameter x and y.
    If game is still playing it returns {"hit": player_attack, "AI_Turn": ai_attack}.
    If game is over it returns {"hit": player_attack, "AI_Turn": ai_attack, 
    'finished': "finish messsage"}.
    """
    if request.args:
        x = request.args.get('x')
        y = request.args.get('y')

        #Player coordinated inputted as (y,x) to frontend
        player_result = g.attack((y, x), players['AI'], battleships['AI'])

        ai_attack = mg.generate_attack(BOARD_SIZE)
        while ai_attack in ai_previous_attacks:
            ai_attack = mg.generate_attack(BOARD_SIZE)

        ai_previous_attacks.append(ai_attack)
        g.attack(ai_attack, players['player'], battleships['player'])

        #Used to check if there exists a ship longer than 0 (not sunk) for both players
        if not any(x != 0 for x in battleships['player'].values()):
            #AI wins
            return {"hit": player_result, "AI_Turn": ai_attack,
                    'finished': "The AI won! Better luck next time"}
        if not any(x != 0 for x in battleships['AI'].values()):
            #Player wins
            return {"hit": player_result, "AI_Turn": ai_attack,
                    'finished': "You won! Congratulaions"}
        #Neither player has won yet
        return {"hit": player_result, "AI_Turn": (ai_attack[1], ai_attack[0])}


if __name__ == '__main__':
    #Initialise battleships dict for player and AI
    battleships['player'] = c.create_battleships()
    battleships['AI'] = c.create_battleships()
    #Create empty boards for player and AI
    players['player'] = c.initialise_board(BOARD_SIZE)
    players['AI'] = c.initialise_board(BOARD_SIZE)

    app.template_folder = "templates"
    app.run()
