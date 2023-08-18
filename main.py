import pygame
from button import Button
from screen import Screen
from gameScreen import gamescreen
from game import Game
from negamax import aiPlayer
from constants import PLAYER


pygame.init()

# frame size
display_height = 600
display_width = 800


# board's coordinate
leftXPosition = 137
boardWidth = 473
rightXPosition = 610
colWidth = 68

# pieces coordinate
top_piece_padding = 383
left_piece_padding = 151
vertical_distance = 59
horizontal_distance = 68


# board screen background image
game_background = pygame.image.load('assets/img/connect four board.png')
game_background = pygame.transform.scale(game_background, (800, 750))
# menu screen background image
menu_background = pygame.image.load('assets/img/menu_background.jpg')
menu_background = pygame.transform.scale(menu_background, (800, 750))

# prevent display from updating fast
clock = pygame.time.Clock()

# create frames
game_screen = gamescreen("Connect 4", display_width,
                         display_height, game_background)
menu = Screen("Menu", display_width, display_height, menu_background)


# menu's logo
logo = pygame.image.load("assets/img/logo.png")
logo = pygame.transform.scale(logo, (500, 175))

# menu objects (like logo, buttons, ...)
button_font = pygame.font.SysFont("Corbel", 25)
start_surface = pygame.image.load("assets/img/startButton.png")
start_hover_surface = pygame.image.load("assets/img/startButton(hover).png")

# game objects (font, ...)
textFont = pygame.font.SysFont("Corbel", 50, bold=True)

# white piece button for menu
wp_surface = pygame.image.load("assets/img/menu white piece.png")
wp_surface = pygame.transform.smoothscale(wp_surface, (60, 60))
wp_clicked_surface = pygame.image.load(
    "assets/img/menu white piece(clicked).png")
wp_clicked_surface = pygame.transform.smoothscale(wp_clicked_surface, (80, 80))

# black piece button for menu
bp_surface = pygame.image.load("assets/img/menu black piece.png")
bp_surface = pygame.transform.smoothscale(bp_surface, (60, 60))
bp_clicked_surface = pygame.image.load(
    "assets/img/menu black piece(clicked).png")
bp_clicked_surface = pygame.transform.smoothscale(bp_clicked_surface, (80, 80))

# buttons for menu
start = Button(start_surface, 400, 480, button_font, menu)
white_button = Button(wp_surface, 320, 340, button_font, menu)
black_button = Button(bp_surface, 470, 340, button_font, menu)


# turn stuff
Human = 0
AI = 1
winner = None


def refreshMenu():  # for reload menu frame
    menu.blit(menu_background, (0, 0))
    menu.blit(logo, (150, 100))  # add logo to menu
    menu.fixed()


menu.makeCurrent()  # first frame(menu)

game_over = False

while not game_over:

    # ----------------------------- MENU FRAME HANDLER --------------------------------
    if menu.checkCurrent():
        if menu.checkEditted():  # if the menu changed
            refreshMenu()   # reload menu's objects
            white_button.update()
            black_button.update()
            start.update()
            pygame.display.update()

        # when we hover on start button
        start.makeShadow(pygame.mouse.get_pos(),
                         start_surface, start_hover_surface)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exit menu screen
                menu.closeScreen()

            if event.type == pygame.MOUSEBUTTONDOWN:  # mouse click

                # check start button clicked
                if start.checkForInput(pygame.mouse.get_pos()):
                    if white_button.checkSelected() or black_button.checkSelected():    # check if any piece has been selected
                        menu.endCurrent()
                        game_screen = gamescreen(
                            "Connect 4", display_width, display_height, game_background)
                        game = Game()
                        if white_button.checkSelected():
                            game_screen.assignPieces("white")
                            turn = Human
                            game.set_turn(PLAYER.Human)
                        elif black_button.checkSelected():
                            game_screen.assignPieces("black")
                            turn = AI
                            game.set_turn(PLAYER.AI)
                        game_screen.makeCurrent()
                        pygame.display.update

                white_button.makeShadow(
                    pygame.mouse.get_pos(), wp_surface, wp_clicked_surface)
                black_button.makeShadow(
                    pygame.mouse.get_pos(), bp_surface, bp_clicked_surface)

    # ----------------------------- GAME FRAME HANDLER --------------------------------
    elif game_screen.checkCurrent():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exit game screen
                game_screen.endCurrent()
                menu.makeCurrent()
                menu.blit(logo, (150, 100))  # add logo to menu
                pygame.display.update()

            if event.type == pygame.MOUSEMOTION:  # mouse movement
                matrix = game.return_matrix()
                game_screen.update(game, matrix)
                posx = event.pos[0]
                if left_piece_padding <= posx <= rightXPosition-10:
                    game_screen.showPiece(posx)
                    pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:    # mouse click
                xposition = event.pos[0]
                if leftXPosition <= xposition <= rightXPosition:
                    if turn == Human:
                        col = (xposition-leftXPosition)//colWidth

                        if game.is_valid_column(col):
                            game.drop(col)
                            game_screen.dropSound.play()  # drop sound
                            matrix = game.return_matrix()
                            game_screen.update(game, matrix)
                            turn = AI
                            # game.preint_matrix()

                        if game.checkWin() == PLAYER.Human:
                            game_over = True
                            winner = "You"

        if turn == AI and not game.gameOver():
            game.drop(aiPlayer(game, 5)[0][0])
            game_screen.dropSound.play()  # drop sound
            if game.checkWin() == PLAYER.AI:
                game_over = True
                winner = "AI"

            # game.preint_matrix()
            matrix = game.return_matrix()
            game_screen.update(game, matrix)
            turn = Human

        if game.check_tie():
            game_over = True

        if game_over:  # show winner texton game screen
            if game.checkWin() == PLAYER.Empty:
                tie_text = textFont.render("Tie", True, (255, 255, 255))
                tie_text_Rect = tie_text.get_rect()
                game_screen.showWinner(tie_text, tie_text_Rect)
                pygame.time.wait(3000)
                break
            Win_text = textFont.render(winner+" Won", True, (255, 255, 255))
            Win_text_Rect = Win_text.get_rect()
            game_screen.showWinner(Win_text, Win_text_Rect)
            pygame.time.wait(3000)

    clock.tick(60)
    pygame.display.update()
