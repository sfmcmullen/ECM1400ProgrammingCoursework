"""Main module"""

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

#TEMPORARY !!!!!!!!!!!!!!!!!!!!!!!
import components as c
ships = c.create_battleships()
board_size = 10
board = c.initialise_board()
board = c.place_battleships(board, ships, 'Custom')


@app.route('/placement', methods = ['GET', 'POST'])
def placement_interface():
    """Placement function"""

    if request.method == 'GET':
        return render_template('placement.html', ships = ships, board_size = board_size)
    
    if request.method == 'POST':
        player_pieces = request.get_json()

        with open('placement.json', 'w') as file:
            json.dump(player_pieces, file)

        return jsonify({"result": True})


@app.route('/', methods = ['GET'])
def root():
    """Root page function"""
    return render_template('main.html', player_board = board)


if __name__ == '__main__':
    app.template_folder = "templates"
    app.run()
