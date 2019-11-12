def coord(m):
    return[ord(m[-2])-96, int(m[-1])]

def check(piece,x,y,table):
    return table[y-1][x-1] == piece

def move(piece,x1,y1,x2,y2,table):
    table[y1-1][x1-1] = 'x'
    table[y2-1][x2-1] = piece

def pawnMove(x,y,color,table):
    if check('x',x,y,table):
        if color == 'w' and y == 4 and check('P',x,y-2,table) and check('x',x,y-1,table):
            move('P',x,y-2,x,y,table)
        elif color == 'b' and y == 5 and check('p',x,y+2,table) and check('x',x,y+1,table):
            move('p',x,y+2,x,y,table)
        elif color == 'w' and check('P',x,y-1,table) and check('x',x,y,table):
            move('P',x,y-1,x,y,table)
        elif color == 'b' and check('p',x,y+1,table):
            move('p',x,y+1,x,y,table)
        else:
            return -1
    return 1

def pawnCapture(x1,x2,y,color,table):
    piece = (lambda p: 'P' if color == 'w' else 'p')(color)
    if color == 'w' and check('P',x1,y-1,table) and check('p',x2,y,table):
        move('P',x1,y-1,x2,y,table)
    elif color == 'b' and check('p',x1,y+1,table) and check('P',x2,y,table):
        move('p',x1,y+1,x2,y,table)
    else:
        return -1
    return 1

def checkKnight(piece,x,y,table):
    positions = [[e,f] for e in range(1,9) for f in range(1,9) if (abs(e-x)==1 and abs(f-y)==2) or (abs(e-x)==2 and abs(f-y)==1)]
    for p in positions:
        if check(piece,p[0],p[1],table):
            return p
    return [-1,-1]

def knightMove(x,y,color,table):
    piece = (lambda p: 'N' if color == 'w' else 'n')(color)
    init_coord = checkKnight(piece,x,y,table)
    if init_coord[0] == -1:
        return -1
    else:
        move(piece,init_coord[0],init_coord[1],x,y,table)
        return 1

def checkDiagonals(piece,diagonals,table):
    for d in diagonals:
        if piece in list(map(lambda coord:table[coord[1]-1][coord[0]-1],d)):
            for coord in d:
                if table[coord[1]-1][coord[0]-1] in ['x',piece]:
                    if table[coord[1]-1][coord[0]-1] == piece:
                        return coord
                else:
                    break
    return [-1,-1]

def checkBishop(piece,x,y,table):
    positions = [[e,f] for e in range(1,9) for f in range(1,9) if (e-x == f-y or e-x == y-f)]
    d1 = [p for p in positions if p[0] < x and p[1] < y][::-1]
    d2 = [p for p in positions if p[0] < x and p[1] > y][::-1]
    d3 = [p for p in positions if p[0] > x and p[1] < y]
    d4 = [p for p in positions if p[0] > x and p[1] > y]
    return checkDiagonals(piece,[d1,d2,d3,d4],table)
        
def bishopMove(x,y,color,table):
    piece = (lambda p: 'B' if color == 'w' else 'b')(color)
    bishop_coord = checkBishop(piece,x,y,table)
    if bishop_coord[0] == -1:
        return -1
    else:
        move(piece,bishop_coord[0],bishop_coord[1],x,y,table)
        return 1

def checkTower(piece,x,y,table):
    positions = [[e,f] for e in range(1,9) for f in range(1,9) if (e == x or f == y) and not(e == x and f == y)]
    l1 = [p for p in positions if p[0] < x and p[1] == y][::-1]
    l2 = [p for p in positions if p[0] > x and p[1] == y]
    l3 = [p for p in positions if p[0] == x and p[1] < y][::-1]
    l4 = [p for p in positions if p[0] == x and p[1] > y]
    return checkDiagonals(piece,[l1,l2,l3,l4],table)

def towerMove(x,y,color,table):
    piece = (lambda p: 'R' if color == 'w' else 'r')(color)
    tower_coord = checkTower(piece,x,y,table)
    if tower_coord[0] == -1:
        return -2
    else:
        move(piece,tower_coord[0],tower_coord[1],x,y,table)
        return 1
    
def checkQueen(piece,x,y,table):
    queen_coord = checkTower(piece,x,y,table)
    if queen_coord[0] == -1:
        queen_coord = checkBishop(piece,x,y,table)
    return queen_coord

def queenMove(x,y,color,table):
    piece = (lambda p: 'Q' if color == 'w' else 'q')(color)
    queen_coord = checkQueen(piece,x,y,table)
    if queen_coord[0] == -1:
        return -1
    else:
        move(piece,queen_coord[0],queen_coord[1],x,y,table)
        return 1

def checkKing(piece,x,y,table):
    positions = [[e,f] for e in range(1,9) for f in range(1,9) if (x-e <= 1 or x-e >= -1) and (y-f <= 1 and y-f >= -1)]
    for p in positions:
        if check(piece,p[0],p[1],table):
            return p
    return -1
    
def kingMove(x,y,color,table):
    piece = (lambda p: 'K' if color == 'w' else 'k')(color)
    king_coord = checkKing(piece,x,y,table)
    if king_coord[0] == -1:
        return -1
    else:
        move(piece,king_coord[0],king_coord[1],x,y,table)
        return 1