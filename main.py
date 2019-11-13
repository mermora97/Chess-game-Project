#!/usr/bin/env python3 

import argparse
from fpdf import FPDF
import src.database as db
import src.api as api
import src.plotting as plot
import src.chessgame as chess
import src.pdf as pdf

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

    mypdf = pdf.FPDF()
    pdf.createPdf(mypdf)

    print('Searching for opening name...')
    opening = db.openingName(config.moves)
    print('You used the opening ',opening)
    mypdf.set_font('Times',size=17)
    mypdf.cell(200, 12, txt='You used the opening: ' + db.openingName(config.moves), ln=3)
    
    print('Printing the following chess positions through the game...')
    fen_list = chess.obtainFenFormat(config.moves)
    probabilities = api.obtainProbabilities(fen_list)
    print('Plotting your probabilities of winning through the game...')
    plot.printProbabilities(probabilities,config.player[0],config.moves)
    print('Looking for an image of the actual chess table position...')
    plot.printChessTable(fen_list[-1])
    print('Creating pdf report with results')
    print('Pdf report with results saved in the Output folder')
    pdf.addImagesToPdf(mypdf)
    pdf.save(mypdf)

if __name__=="__main__":
    main()