import requests
import json
import src.chessgame as chess
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def chessRequest(fen,nextMoves = 5):
    url = 'https://explorer.lichess.ovh/master?moves={}&fen={}'.format(str(nextMoves),fen)
    return requests.get(url).json()


def probabilities(data):
    total = sum([data['white'], data['black'], data['draws']])
    whites = data['white']
    draws = data['draws']
    blacks = data['black']
    return [round(whites*100/total,2), round(draws*100/total,2), round(blacks*100/total,2)]

def obtainProbabilities(fens):
    probs = []
    for fen in fens:
        data = chessRequest(fen)
        if data['topGames']:
            probs.append(probabilities(data))
    return probs