from constants import *
from game import Game

def evaluate(board:Game): 
    # Is final state?
    boardState = board.checkWin()
    if boardState == PLAYER.Human: return infinity if board.turn == PLAYER.Human else -infinity
    elif boardState == PLAYER.AI: return -infinity if board.turn == PLAYER.Human else infinity
    elif boardState == PLAYER.Empty: return 0
    
    scorelist = [] # [human, ai]
    
    for player in [PLAYER.Human, PLAYER.AI]:
        score = 0
        # Horizontal
        for y in range(board.rowCount):
            for x in range(board.colCount - 3):
                if board.matrix[y][x] == player or board.matrix[y][x] == PLAYER.Empty:
                    if board.matrix[y][x + 1] == player or board.matrix[y][x + 1] == PLAYER.Empty:
                        if board.matrix[y][x + 2] == player or board.matrix[y][x + 2] == PLAYER.Empty:  
                            if board.matrix[y][x + 3] == player or board.matrix[y][x + 3] == PLAYER.Empty:  
                                score += 1
        
        # Vertical
        for x in range(board.colCount):
            for y in range(board.rowCount - 3):
                if board.matrix[y][x] == player or board.matrix[y][x] == PLAYER.Empty:
                    if board.matrix[y + 1][x] == player or board.matrix[y + 1][x] == PLAYER.Empty:
                        if board.matrix[y + 2][x] == player or board.matrix[y + 2][x] == PLAYER.Empty:  
                            if board.matrix[y + 3][x] == player or board.matrix[y + 3][x] == PLAYER.Empty:  
                                score += 1
        
        # Diagonal \
        for y in range(board.rowCount - 3):
            for x in range(board.colCount - 3):
                if board.matrix[y][x] == player or board.matrix[y][x] == PLAYER.Empty:
                    if board.matrix[y + 1][x + 1] == player or board.matrix[y + 1][x + 1] == PLAYER.Empty:
                        if board.matrix[y + 2][x + 2] == player or board.matrix[y + 2][x + 2] == PLAYER.Empty:  
                            if board.matrix[y + 3][x + 3] == player or board.matrix[y + 3][x + 3] == PLAYER.Empty:  
                                score += 1
        
        # Diagonal /
        for y in range(3, board.rowCount):
            for x in range(board.colCount - 3):
                if board.matrix[y][x] == player or board.matrix[y][x] == PLAYER.Empty:
                    if board.matrix[y - 1][x + 1] == player or board.matrix[y - 1][x + 1] == PLAYER.Empty:
                        if board.matrix[y - 2][x + 2] == player or board.matrix[y - 2][x + 2] == PLAYER.Empty:  
                            if board.matrix[y - 3][x + 3] == player or board.matrix[y - 3][x + 3] == PLAYER.Empty:  
                                score += 1
        
        scorelist.append(score)
    
    if board.turn == PLAYER.Human:
        return scorelist[0] - scorelist[1]
    
    return scorelist[1] - scorelist[0]