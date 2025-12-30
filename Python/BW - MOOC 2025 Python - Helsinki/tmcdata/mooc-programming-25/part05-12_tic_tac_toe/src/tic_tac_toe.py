def play_turn(game_board: list, x:int, y: int, piece: str):
    
    if x < 0:
        return False
    if x > 2:
        return False
    if y < 0:
        return False
    if y > 2:
        return False

    while 0 <= x < 3 and 0 <= y < 3:
        if game_board[x][y] == '':
            game_board[x][y] = piece
            return True

        elif game_board[x][y] == piece:
            return False
        else:
            return False

