"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
AI = ""


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Player = {
        "X": 0, "O": 0
    }
    for i in board:
        for j in i:
            if j == "X":
                Player["X"] += 1
            elif j == "O":
                Player["O"] += 1
    if Player["X"] > Player["O"]:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    final = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                final.append([i, j])
    return final


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action[0], action[1]
    boardCopy = copy.deepcopy(board)
    boardCopy[i][j] = player(board)
    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and bool(board[0][0]):
        return board[0][0]
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and bool(board[0][0]):
        return board[0][0]
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and bool(board[0][0]):
        return board[0][0]
    elif board[1][1] == board[0][1] and board[0][1] == board[2][1] and bool(board[1][1]):
        return board[1][1]
    elif board[1][1] == board[1][0] and board[1][2] == board[1][0] and bool(board[1][1]):
        return board[1][1]
    elif board[1][1] == board[0][2] and board[0][2] == board[2][0] and bool(board[1][1]):
        return board[1][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and bool(board[2][2]):
        return board[2][2]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and bool(board[2][2]):
        return board[2][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerFinal = winner(board)
    if winnerFinal == X:
        return 1
    elif winnerFinal == O:
        return -1
    else:
        return 0


def MaxValue(board):
    if terminal(board):
        return utility(board)

    v = -10000000000
    for action in actions(board):
        v = max(v, MinValue(result(board, action)))
    return v


def MinValue(board):
    if terminal(board):
        return utility(board)

    v = 10000000000
    for action in actions(board):
        v = min(v, MaxValue(result(board, action)))
    return v


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

    return None

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    results = {}
    key = {}
    plyr = player(board)

    if plyr == O:
        for action in actions(board):
            results[str(action)] = min(100000000, MaxValue(result(board, action)))
            key[str(action)] = action
            print(results)
        if(get_key(-1, results) == None):
            if get_key(0, results) == None:
                return results[1]
            else:
                return key[get_key(0, results)]
        else:
            return key[get_key(-1, results)]
    else:
        for action in actions(board):
            results[str(action)] = max(-100000000, MinValue(result(board, action)))
            key[str(action)] = action
            print(results)
        if (get_key(1, results) == None):
            if get_key(0, results) == None:
                return results[-1]
            else:
                return key[get_key(0, results)]
        else:
            return key[get_key(1, results)]

