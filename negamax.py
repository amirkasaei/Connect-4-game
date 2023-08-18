from evaluate import evaluate
from game import Game
from constants import *


def tuple2element(inp: tuple) -> int:
    return inp[1][0]


def negamax(board: Game, depth: int, alpha: float, beta: float, step: int) -> float:
    level = step + 1
    if depth == 0 or board.checkWin() != None:
        return evaluate(board), level

    for move in board.getMoves():
        board.drop(move)
        score, level = negamax(board, depth - 1, -beta, -alpha, step+1)
        score = -score
        board.undo(move)
        if score >= beta:
            return beta, level

        alpha = max(score, alpha)
    return alpha, level


def aiPlayer(board: Game, depth: int) -> list[tuple]:
    moveRating = []
    for move in board.getMoves():
        board.drop(move)
        moveRating.append(
            (move, negamax(board, depth, -infinity, infinity, 0)))
        board.undo(move)
    sortedMoves = sorted(moveRating, key=lambda moveRating: (
        moveRating[1][0], moveRating[1][1]))
    print(sortedMoves)
    return sortedMoves
