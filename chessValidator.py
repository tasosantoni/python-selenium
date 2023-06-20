# Function isValidChessBoard checks whether a given chess board is valid or not.
# Returns True if valid or False if not.

def isValidChessBoard(board):

    players = ('w', 'b')
    pieces = ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king')
    numPieces = {}
    spaces = []
    valid_letters = ('a','b','c','d','e','f','g','h')
    validBoard = True

    for i in range(8):
        for j in range(8):
            spaces.append(str(i+1) + valid_letters[j])

    for k,v in board.items():
        if k not in spaces:
            print('Wrong space name ' + k + ' detected.')
            validBoard = False
        if v[0] not in players:
            print('Wrong player name ' + v[0] + ' detected.')
            validBoard = False
        if v[1:] not in pieces:
            print('Wrong piece name ' + v[1:] + ' detected.')
            validBoard = False

    for v in board.values():
        numPieces.setdefault(v, 0)
        numPieces[v] += 1

    if numPieces.get('wking', 0) > 1:
        print('A valid board can have exactly one white king!')
        validBoard = False
    if numPieces.get('bking', 0) > 1:
        print('A valid board can have exactly one black king!')
        validBoard = False
    if numPieces.get('wqueen', 0) > 1:
        print('A valid board can have exactly one white queen!')
        validBoard = False
    if numPieces.get('bqueen', 0) > 1:
        print('A valid board can have exactly one black queen!')
        validBoard = False
    if numPieces.get('wknight', 0) > 2:
        print('A valid board can have two white knights at most!')
        validBoard = False
    if numPieces.get('bknight', 0) > 2:
        print('A valid board can have two black knights at most!')
        validBoard = False
    if numPieces.get('wbishop', 0) > 2:
        print('A valid board can have two white bishops at most!')
        validBoard = False
    if numPieces.get('bbishop', 0) > 2:
        print('A valid board can have two black bishops at most!')
        validBoard = False
    if numPieces.get('wrook', 0) > 2:
        print('A valid board can have two white rooks at most!')
        validBoard = False
    if numPieces.get('brook', 0) > 2:
        print('A valid board can have two black rooks at most!')
        validBoard = False
    if numPieces.get('wpawn', 0) > 8:
        print('A valid board can have eight white pawns at most!')
        validBoard = False
    if numPieces.get('bpawn', 0) > 8:
        print('A valid board can have eight black pawns at most!')
        validBoard = False

    white_pieces = numPieces.get('wking', 0) + numPieces.get('wqueen', 0) + numPieces.get('wknight', 0) \
                 + numPieces.get('wbishop', 0) + numPieces.get('wrook', 0) + numPieces.get('wpawn', 0)

    black_pieces = numPieces.get('bking', 0) + numPieces.get('bqueen', 0) + numPieces.get('bknight', 0) \
                 + numPieces.get('bbishop', 0) + numPieces.get('brook', 0) + numPieces.get('bpawn', 0)

    if white_pieces > 16:
        print('A valid board can have sixteen white pieces at most!')
        validBoard = False
    if black_pieces > 16:
        print('A valid board can have sixteen black pieces at most!')
        validBoard = False

    if validBoard == False:
        print('The given chess board is invalid!!!')
        return False
    else:
        print('The given chess board is valid!!!')
        return True


#Practice board
b = {'1g': 'bking', '2f': 'wking', '3h': 'wqueen', '3f': 'bpawn', '4f': 'bpawn', '5f': 'bpawn', '6f': 'bpawn', '7f': 'bpawn', '8f': 'bpawn', '7h': 'bpawn', '5h': 'bpawn','1f': 'bpawn'}
isValidChessBoard(b)
