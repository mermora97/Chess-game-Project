#!/usr/bin/env python3 

import sys
import argparse
import subprocess
import src.api as api
import src.plotting as plot
import src.chessgame as chess

def recibeConfig():
    parser = argparse.ArgumentParser(description='Evaluate the evolution of a chess game')
    parser.add_argument('--player',
                        help='White / black chess player',
                        default='white'
                        )
    parser.add_argument('moves',nargs='+',
                        help='Chess moves performed',
                        )                 
    return parser.parse_args()

def main():
    # Pipeline
        
    # PASO 1 - Recibir flags y estandarizarlos en un dict
    config = recibeConfig()    
    probabilities = api.obtainProbabilities(config.moves)
    plot.printProbabilities(probabilities,config.moves)
    fen = chess.obtainFenFormat(config.moves)[-1]
    plot.printChessTable(fen)

if __name__=="__main__":
    main()