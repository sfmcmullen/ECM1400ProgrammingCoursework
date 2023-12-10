"""Main module"""

import json
from flask import Flask, render_template, request
import components as c
import game_engine as g
import mp_game_engine as mg

app = Flask(__name__)

#Stores the ships in use this game.
# Not to be confused for the battleships dict that stores the individual player ship values.
ships = c.create_battleships()
#Dictionary of players. Key = Username, Value = Board
players = {}
#Stores the values of previous attacks for generate_attack
ai_previous_attacks = []
#Stores the battleships for the user and AI
battleships = {}
#Stores the size of the board in use
BOARD_SIZE = 10


@app.route('/placement', methods = ['GET', 'POST'])
def placement_interface():
    """Placement function"""

    if request.method == 'GET':
        return render_template('placement.html', ships = ships, board_size = BOARD_SIZE)

    if request.method == 'POST':
        player_pieces = request.get_json()

        with open('placement.json', 'w') as file:
            json.dump(player_pieces, file)

        #Adds pieces to user board from placement.json
        players['player'] = c.place_battleships(players['player'], ships, 'Custom')
        #adds random pieces to AI board
        players['AI'] = c.place_battleships(players['AI'], ships, 'Random')

        return {"result": True}


@app.route('/', methods = ['GET'])
def root():
    """Root page function"""

    return render_template('main.html', player_board = players['player'])


@app.route('/attack', methods = ['GET'])
def process_attack():
    """Attack function"""
    if request.args:
        x = request.args.get('x')
        y = request.args.get('y')

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
        return {"hit": player_result, "AI_Turn": ai_attack}


if __name__ == '__main__':
    #Initialise battleships dict for player and AI
    battleships['player'] = c.create_battleships()
    battleships['AI'] = c.create_battleships()
    #Create empty boards for player and AI
    players['player'] = c.initialise_board()
    players['AI'] = c.initialise_board()

    app.template_folder = "templates"
    app.run()
