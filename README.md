# Chess-game-Project

In this project, a program is developed in Python language to analyze the development of a chess game-

The program takes the following inputs:

- Chess player (white/black) (optional) : default value = 'white'
- Chess moves written in algebraic chess notation 

Some examples are:

main.py --player white e4 e5 Nf3 d6 d4 Bg4 d4xe5
main.py e4 e5 Nf3 Nc6 Bc4 Bc5 c3 Nf6 d4


# Files organization

Files are organised as follow:

Input - Input folder contains the initial database csv that will be analyzed to obtain the name of the game opening eg: 'Slav Defense' 1.d4 d5 2.c4 c6

Output - In this folder, 4 different files are saved: the modified input database, a plot representing the winning probabilities of the player in the different moves, an image of the current chess table position and a pdf file containing the previous information.

src - The src folder contains the python files where the main functionality of the program is stored.

main.py - My program

README.md - Instructions

# Pipelines

A database called 'games.csv' was downloaded from Kaggle and used to study the chess opening of the game.

The api https://lichess.org/api is used to execute requests in games with the same moves as the one introduce in order to study the probabilities of winning and losing of the player. The input of the request is the chess table position in FEN (Forsyth-Edwards Notation). A new request is made for each move in the game. At the same time, every time a move is performed, the table position is printed in the terminal screen.

To implement the techniques learned in web scraping, a screenshot of the final chess position is obtained from  https://www.dcode.fr/fen-chess-notation with Selenium webscraping.

Finally, all the obtained information will be saved on PDF format on the Output folder.
