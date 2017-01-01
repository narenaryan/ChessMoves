import argparse, json

chessBoard = [[1, 1, 1, 1, 1, 1, 1, 1] for i in range(8)]

chess_map_from_alpha_to_index = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7
}

chess_map_from_index_to_alpha = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h"
}


def getRookMoves(pos, chessBoard):
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_alpha_to_index[column]
    i,j = row, column
    solutionMoves = []

    # Compute the moves in Rank
    for j in xrange(8):
        if j != column:
            solutionMoves.append((row, j))

    # Compute the moves in File
    for i in xrange(8):
        if i != row:
           solutionMoves.append((i, column))

    solutionMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in solutionMoves]
    solutionMoves.sort()
    return solutionMoves

def getKnightMoves(pos, chessBoard):
    """ A function that returns the all possible moves
        of a knight stood on a given position
    """
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_alpha_to_index[column]
    i,j = row, column
    solutionMoves = []
    try:
        temp = chessBoard[i + 1][j - 2]
        solutionMoves.append([i + 1, j - 2])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j - 1]
        solutionMoves.append([i + 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j + 1]
        solutionMoves.append([i + 2, j + 1])
    except:
        pass
    try:
        temp = chessBoard[i + 1][j + 2]
        solutionMoves.append([i + 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j + 2]
        solutionMoves.append([i - 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j + 1]
        solutionMoves.append([i - 2, j + 1])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j - 1]
        solutionMoves.append([i - 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j - 2]
        solutionMoves.append([i - 1, j - 2])
    except:
        pass

    # Filter all negative values
    temp = [i for i in solutionMoves if i[0] >=0 and i[1] >=0]
    allPossibleMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    allPossibleMoves.sort()
    return allPossibleMoves

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--piece", help="chess piece name: ex- rook, knight, pawn etc")
parser.add_argument("-l", "--location", help="chess notation string: ex- E4, D6 etc")
args = parser.parse_args()

piece = args.piece.strip().lower()
location = args.location.strip()
# According to the type of piece adjust function
if (piece == "rook"):
    print json.dumps({"piece":piece,
                      "current_location": location,
                      "moves": getRookMoves(location, chessBoard)})
elif (piece == "knight"):
    print json.dumps({"piece":piece,
                      "current_location": location,
                      "moves": getKnightMoves(location, chessBoard)})


