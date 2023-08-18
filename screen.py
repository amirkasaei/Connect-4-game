import sys
import pygame


class Screen():
    def __init__(self, title, width, height, backgroundImage):
        self.title = title
        self.width = width
        self.height = height
        self.backgroundImage = backgroundImage
        self.current = False
        self.edit = True

    def makeCurrent(self):  # make screen on top
        pygame.display.set_caption(self.title)
        self.current = True
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.blit(self.backgroundImage, (0, 0))

    def checkCurrent(self):  # check if a screen is on top
        return self.current

    def endCurrent(self):  # make screen off top
        self.current = False

    def blit(self, object, position):  # build given object in screen
        self.screen.blit(object, position)
        pygame.display.update()

    def fixed(self):    # if the changes were applied
        self.edit = False

    def editted(self):  # if the screen has changed
        self.edit = True

    def checkEditted(self):  # check screen whether need to change or not
        return self.edit

    def closeScreen(self): # close the screen
        pygame.quit()
        sys.exit()
