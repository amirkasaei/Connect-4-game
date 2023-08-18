class Button():
    def __init__(self, image, x_pos, y_pos, buttonFont, screen):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.font = buttonFont
        self.screen = screen
        self.state = "out"
        self.selected = False

    def update(self):   # blit button in the screen
        self.screen.blit(self.image, self.rect)

    # if the mouse position is on the button area
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeSelected(self):   # when we hover or clicked on a button
        if self.selected:
            self.selected = False
        else:
            self.selected = True

    def checkSelected(self):    # get button's selected variable
        return self.selected

    def makeShadow(self, position, surface, hoverSurface):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):  # on the bottun
            if self.state == "out":
                self.state = "in"
                self.image = hoverSurface
                self.changeSelected()
                self.screen.editted()

        else:   # out of the button
            if self.state == "in":
                self.state = "out"
                self.image = surface
                self.changeSelected()
                self.screen.editted()
