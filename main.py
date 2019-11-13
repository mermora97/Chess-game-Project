#!/usr/bin/env python3 

import argparse
import src.database as db
import src.api as api
import src.plotting as plot
import src.chessgame as chess

def recibeConfig():
    parser = argparse.ArgumentParser(description='Evaluate the evolution of a chess game')
    parser.add_argument('--player',
                        choices=['white','black'],
                        help='white or black chess player',
                        default='white'
                        )
    parser.add_argument('moves',nargs='+',
                        help='Chess moves performed',
                        )                 
    return parser.parse_args()

def main():

    # Pipeline        
    config = recibeConfig()
    print('Searching for opening name...')
    print('You used the opening ',db.openingName(config.moves))
    print('Searching your probabilities of winning in each move...')
    fen_list = chess.obtainFenFormat(config.moves)
    probabilities = api.obtainProbabilities(fen_list)
    print('Plotting the probabilities through the game...')
    plot.printProbabilities(probabilities,config.player[0],config.moves)
    print('Looking for an image of the actual chess table position...')
    plot.printChessTable(fen_list[-1])

if __name__=="__main__":
    main()