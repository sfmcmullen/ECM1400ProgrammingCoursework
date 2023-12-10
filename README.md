# Battleships

***


### Introduction

This is a one-player game of battleships against an AI opponent. It utilizes a web interface in which the player will configure their board and then attack the AI opponent.


### Prerequisites

Before running the code you must have a version of Python installed on your computer. This program was developed on Python 3.12.0.  
You must also have a web browser application such as Google Chrome.

### Installation

You will have to run the following commands in the command prompt to have all available modules that aren't part of the regular Python package.  
`pip install flask`  
`pip install pytest`


### Getting Started

Run the code from the terminal by typing ``python main.py`` from within the Battleships directory.  
A link similar to http://127.0.0.1:5000 will be displayed within the terminal window. Click on the link to open the game in a web browser, or just type the displayed link into your browser.  
Then access the placement path by appending */placement* to the end of your URL in your browser. For example from the root path http://127.0.0.1:5000/ we have here you would enter http://127.0.0.1:5000/placement.  
Once you have completed the placement and submitted your grid you will be redirected to the root page where you will then be able to commence attacks on the opponent's grid until either you or the opponent has won the game.


### Testing

To test that the code is running correctly on your device there is a folder in the Battleships directory called tests. From there there are several modules to test different aspects of the code.  
If using VS code to run the program you can use the Python test manager (flask icon on sidebar) and configure it so that the test folder is the *tests* folder from the current Battleships directory. Then just run the tests folder within the test manager using the play button and if any test fails you will be able to see the test and its error. For other IDEs, you should use their respective test managers to run the tests in a similar fashion.


### Developer Documentation

The program is split into four modules:
- `components.py`
- `game_engine.py`
- `mp_game_engine.py`
- `main.py`

The `components.py` module stores the functions that are used to initialize a `simple_game_loop` or `ai_opponent_game_loop` such as initializing the boards and placing the battleships.  
The `game_engine.py` module contains the functions used for a `simple_game_loop` gameplay mechanics, such as getting coordinate inputs from the user or attacking the board.  
The `mp_game_engine.py` module contains the additional functions used for a `ai_opponent_game_loop` gameplay mechanics such as displaying the user's board and generating ai attacks that attack the user's board.  
The `main.py` module utilizes the previous modules' functions through a Flask web interface to ultimately produce the online battleships game.  

### Details

Author: Samuel McMullen  
Source code: https://github.com/sfmcmullen/ECM1400ProgrammingCoursework  
Acknowledgments: This was the coursework project made for ECM1400 at Exeter University