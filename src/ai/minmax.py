def find_best_move(game):
    best_score = float("-inf")
    best_move = None

    for move in game.get_empty_cells():
        row, col = move
        game.board[row][col] = -1
        score = minimax(game, 0, False)
        game.board[row][col] = 0

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def minimax(game, depth, is_maximizing):
    if game.is_winner(-1):
        return 10 - depth
    if game.is_winner(1):
        return depth - 10
    if game.is_draw():
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for move in game.get_empty_cells():
            row, col = move
            game.board[row][col] = -1
            score = minimax(game, depth + 1, False)
            game.board[row][col] = 0
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in game.get_empty_cells():
            row, col = move
            game.board[row][col] = 1
            score = minimax(game, depth + 1, True)
            game.board[row][col] = 0
            best_score = min(score, best_score)
        return best_score
