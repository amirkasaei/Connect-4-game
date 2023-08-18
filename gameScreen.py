import pygame
import numpy as np
from screen import Screen
from game import Game
from constants import *

# pieces coordinate
top_piece_padding = 383
left_piece_padding = 151
vertical_distance = 59
horizontal_distance = 68

# Piece images
white_piece = pygame.image.load('assets/img/white piece.png')
white_piece = pygame.transform.scale(white_piece, (44, 44))
black_piece = pygame.image.load('assets/img/black piece.png')
black_piece = pygame.transform.scale(black_piece, (44, 44))

PLAYER_PIECE = 1  # number in the matrix board
AI_PIECE = 2  # number in the matrix board
Empty = 0  # Empty element


class gamescreen(Screen):
    def __init__(self, title, width, rowCount, backgroundImage):
        super().__init__(title, width, rowCount, backgroundImage)
        self.dropSound = pygame.mixer.Sound(
            'assets/sound/wooden_piece_falling_01.wav')

    def assignPieces(self, playerPiece): # assign selected piece to player
        if playerPiece == "black": 
            self.player_piece = black_piece
            self.AI_piece = white_piece
        else:  # playerPiece == "white"
            self.player_piece = white_piece
            self.AI_piece = black_piece

    def update(self, board: Game, matrix): # update game board
        matrix = np.flip(matrix, 0)
        self.makeCurrent()
        for col in range(board.colCount):
            for row in range(board.rowCount):
                if int(matrix[row][col]) == PLAYER_PIECE:
                    self.screen.blit(
                        self.player_piece, (left_piece_padding + col * horizontal_distance,
                                            top_piece_padding - row * vertical_distance))
                elif int(matrix[row][col]) == AI_PIECE:  # AI turns
                    self.screen.blit(
                        self.AI_piece, (left_piece_padding + col * horizontal_distance,
                                        top_piece_padding - row * vertical_distance))
        pygame.display.update()

    def showPiece(self, mouseXposition):
        self.screen.blit(self.player_piece, (mouseXposition - 22, 10))
        pygame.display.update()

    def showWinner(self, winner_text, Win_text_Rect):
        Win_text_Rect.center = (380, 500)
        self.screen.blit(winner_text, Win_text_Rect)
        pygame.display.update()
