def empty_indices(board):
    return [x for x in board if (x != 'O' and x != 'X')]

def won(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
        (board[3] == player and board[4] == player and board[5] == player) or \
        (board[6] == player and board[7] == player and board[8] == player) or  \
        (board[0] == player and board[3] == player and board[6] == player) or   \
        (board[1] == player and board[4] == player and board[7] == player) or    \
        (board[2] == player and board[5] == player and board[8] == player) or     \
        (board[0] == player and board[4] == player and board[8] == player) or      \
        (board[2] == player and board[4] == player and board[6] == player) :
            return True
    return False

def minimax(new_board, player):
    global Human, AI
    availspots = empty_indices(new_board)
    #print (availspots)
    if won(new_board, Human):
        return {'score':-10}
    elif won(new_board, AI):
        return {'score':10}
    elif len(availspots) == 0:
        return {'score':0}

    moves = []

    for i in range(len(availspots)):
        move = {}
        move['index'] = new_board[availspots[i]]
        new_board[availspots[i]] = player

        if player == AI:
            result = minimax(new_board, Human)
            move['score'] = result['score']
        else:
            result = minimax(new_board, AI)
            move['score'] = result['score']
        
        new_board[availspots[i]] = move['index']

        moves.append(move)

    best_move = None
    if player == AI:
        best_score = -10000
        for i in range(len(moves)):
            if moves[i]['score'] > best_score:
                best_score = moves[i]['score']
                best_move = i
    else:
        best_score = 10000
        for i in range(len(moves)):
            if moves[i]['score'] < best_score:
                best_score = moves[i]['score']
                best_move = i


    return moves[best_move]


Human = 'O'
AI = 'X'

def main():
    pass


if __name__ == "__main__":
    main()
