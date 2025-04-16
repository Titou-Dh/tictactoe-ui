def find_best_move_ab(game):
    best_score = float("-inf")
    best_move = None
    alpha = float("-inf")
    beta = float("inf")

    for move in game.get_empty_cells():
        row, col = move
        game.board[row][col] = -1
        score = alphabeta(game, 0, False, alpha, beta)
        game.board[row][col] = 0

        if score > best_score:
            best_score = score
            best_move = move

        alpha = max(alpha, best_score)

    return best_move


def alphabeta(game, depth, is_maximizing, alpha, beta):
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
            score = alphabeta(game, depth + 1, False, alpha, beta)
            game.board[row][col] = 0
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float("inf")
        for move in game.get_empty_cells():
            row, col = move
            game.board[row][col] = 1
            score = alphabeta(game, depth + 1, True, alpha, beta)
            game.board[row][col] = 0
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score
