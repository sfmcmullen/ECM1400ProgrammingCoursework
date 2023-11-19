"""Main module"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/placement')
def placement_interface():
    return render_template('placement.html', title='Placement')


if __name__ == '__main__':
    app.run()