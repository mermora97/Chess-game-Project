import src.chessfunction as cfn
import re

def move(m,color,table):
    x = cfn.coord(m)[0]
    y = cfn.coord(m)[1]

    if len(m) == 2:
        return cfn.pawnMove(x,y,color,table)
    elif m[0] == 'C':
        return cfn.knightMove(x,y,color,table)
    elif m[0] == 'A':
        return cfn.bishopMove(x,y,color,table)
    elif m[0] == 'T':
        return cfn.towerMove(x,y,color,table)
    elif m[0] == 'D':
        return cfn.queenMove(x,y,color,table)
    elif m[0] == 'R':
        return cfn.kingMove(x,y,color,table)
    elif (m[0] in [chr(e) for e in range(97,123)]):
        x1 = cfn.coord(m[0]+'0')[0]
        return cfn.pawnCapture(x1,x,y,color,table)
    return -1

def moveChessPieces(m,color,table):
    if move(m,color,table) == -1:
        raise ValueError('Move '+m+' is not allowed.')
    
    resulted_table = '/'.join([''.join(e) for e in table][::-1])
    
    for i in range(0,8):
        x = ''.join(['x' for i in range(8-i)])
        resulted_table = resulted_table.replace(x,str(8-i))
    #print('\n'.join([''.join(e) for e in table]))
    return resulted_table

def changeColor(color):
    return (lambda c:'w' if c == 'b' else 'b')(color)

def obtainFenFormat(chessgame):

    table = 'rnbqkbnr\npppppppp\nxxxxxxxx\nxxxxxxxx\nxxxxxxxx\nxxxxxxxx\nPPPPPPPP\nRNBQKBNR'
    table = [re.findall('.',r) for r in table.split('\n')[::-1]]

    count = 1
    halfCount = 0
    color = 'b'

    fens = []
    for m in chessgame:
        color = changeColor(color)
        fen = moveChessPieces(m,color,table)

        if re.search('x',m) or re.search('^[a-h]',m):
            halfCount = 0
        else:
            halfCount += 1
        count += 1 

        fen = fen + '%20' + changeColor(color) + '%20KQkq%20'

        if color == 'w' and re.search('[a-h]4',m):
            fen = fen + m[0] + '3' + '%20'
        elif  (color == 'b' and re.search('[a-h]5',m)):
            fen = fen + m[0] + '4' + '%20'
        else:
            fen = fen + '-' + '%20'
        fen = fen + str(halfCount) + '%20' + str(int(count/2))
        fens.append(fen)
        print('\n'+'\n'.join([''.join(e) for e in table])+'\n')
    return fens