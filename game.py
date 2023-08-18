from constants import *


class Game():
    colCount = 7
    rowCount = 6

    def __init__(self) -> None:
        self.matrix = [[PLAYER.Empty for _ in range(
            self.colCount)] for _ in range(self.rowCount)]
        

    def return_matrix(self):
        return self.matrix
    
    def set_turn(self, turn):
        self.turn = turn

    def preint_matrix(self) -> None:
        for y in range(self.rowCount):
            prntx = ""
            for x in range(self.colCount):
                prntx += self.matrix[y][x] + "  "
            print(prntx)

    def drop(self, x: int) -> None:
        for y in range(self.rowCount - 1, -1, -1):
            if self.matrix[y][x] == PLAYER.Empty:
                self.matrix[y][x] = self.turn
                self.turn = PLAYER.AI if self.turn == PLAYER.Human else PLAYER.Human
                return 0

        assert False

    def is_valid_column(self, x):
        for y in range(self.rowCount - 1, -1, -1):
            if self.matrix[y][x] == PLAYER.Empty:
                return True

    def gameOver(self):
        return False

    def undo(self, x: int) -> None:
        for y in range(self.rowCount):
            if self.matrix[y][x] != PLAYER.Empty:
                self.matrix[y][x] = PLAYER.Empty
                self.turn = PLAYER.AI if self.turn == PLAYER.Human else PLAYER.Human
                return 0

        assert False

    def getMoves(self) -> list:
        movList = []
        for x in range(self.colCount):
            if self.matrix[0][x] == PLAYER.Empty:
                movList.append(x)

        return movList

    def checkWin(self) -> PLAYER:
        # Horizontal
        for y in range(self.rowCount):
            for x in range(self.colCount - 3):
                if self.matrix[y][x] == self.matrix[y][x + 1] == self.matrix[y][x + 2] == self.matrix[y][x + 3] != PLAYER.Empty:
                    return self.matrix[y][x]

        # Vertical
        for x in range(self.colCount):
            for y in range(self.rowCount - 3):
                if self.matrix[y][x] == self.matrix[y + 1][x] == self.matrix[y + 2][x] == self.matrix[y + 3][x] != PLAYER.Empty:
                    return self.matrix[y][x]

        # Diagonal \
        for x in range(self.colCount - 3):
            for y in range(self.rowCount - 3):
                if self.matrix[y][x] == self.matrix[y+1][x+1] == self.matrix[y+2][x+2] == self.matrix[y+3][x+3] != PLAYER.Empty:
                    return self.matrix[y][x]

        # Diagonal /
        for y in range(self.rowCount - 3):
            for x in range(3, self.colCount - 1):
                if self.matrix[y][x] == self.matrix[y+1][x-1] == self.matrix[y+2][x-2] == self.matrix[y+3][x-3] != PLAYER.Empty:
                    return self.matrix[y][x]

        # Not done
        for x in range(self.colCount):
            for y in range(self.rowCount):
                if self.matrix[y][x] == PLAYER.Empty:
                    return None

        # Tie
        return PLAYER.Empty
    
    def check_tie(self):
        tie = True
        for col in range(7):
            if self.is_valid_column(col):
                tie = False
                return tie
        return tie
                
