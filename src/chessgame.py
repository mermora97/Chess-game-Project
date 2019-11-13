import re
import src.chessfunction as fn

def movePiece(m,color,table):
    x = fn.coord(m)[0]
    y = fn.coord(m)[1]

    if len(m) == 2:
        return fn.pawnMove(x,y,color,table)
    elif m[0] == 'N':
        return fn.knightMove(x,y,color,table)
    elif m[0] == 'B':
        return fn.bishopMove(x,y,color,table)
    elif m[0] == 'R':
        return fn.towerMove(x,y,color,table)
    elif m[0] == 'Q':
        return fn.queenMove(x,y,color,table)
    elif m[0] == 'K':
        return fn.kingMove(x,y,color,table)
    elif (m[0] in [chr(e) for e in range(97,123)]):
        x1 = fn.coord(m[0]+'0')[0]
        return fn.pawnCapture(x1,x,y,color,table)
    return -1

def substituteXs(string):
    for i in range(8,0,-1):
        x = ''.join(['x' for i in range(i)])
        string = string.replace(x,str(i))
    return string
   
def moveChessPieces(m,color,table):
    if movePiece(m,color,table) == -1:
        raise ValueError('Move '+ m +' is not allowed.')
    
    fen_table = '/'.join([''.join(e) for e in table][::-1])
    return substituteXs(fen_table)

def printRealisticTable(m,count,table):
    #Heading
    print('----------------')
    print(str(int(count/2)) + '. ' + m)

    #Chess table
    table = '\n'.join([' '.join(e) for e in table])
    table = table.replace('K','♔').replace('k','♚').replace(
        'Q','♕').replace('q','♛').replace('R','♖').replace(
            'r','♜').replace('N','♘').replace('n','♞').replace(
                'B','♗').replace('b','♝').replace('P','♙').replace(
                    'p','♟').replace('x',' ')
    print('\n'+ table +'\n')

def switchColor(color):
    return (lambda c:'w' if c == 'b' else 'b')(color)

def obtainFenFormat(chessgame):

    table = 'rnbqkbnr\npppppppp\nxxxxxxxx\nxxxxxxxx\nxxxxxxxx\nxxxxxxxx\nPPPPPPPP\nRNBQKBNR'
    table = [re.findall('.',r) for r in table.split('\n')[::-1]]

    count = 1
    halfCount = 0
    color = 'b'

    fens = []
    for m in chessgame:
        color = switchColor(color)
        fen = moveChessPieces(m,color,table)

        if re.search('x',m) or re.search('^[a-h]',m):
            halfCount = 0
        else:
            halfCount += 1
        count += 1

        fen = fen + '%20' + switchColor(color) + '%20KQkq%20'

        if color == 'w' and re.search('[a-h]4',m):
            fen = fen + m[0] + '3' + '%20'
        elif  (color == 'b' and re.search('[a-h]5',m)):
            fen = fen + m[0] + '4' + '%20'
        else:
            fen = fen + '-' + '%20'
        fen = fen + str(halfCount) + '%20' + str(int(count/2))
        fens.append(fen)
        printRealisticTable(m,count, table)
    return fens