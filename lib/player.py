from lib.managers import InputManager

class PlayerMovement:
    def __init__(self):
        self.moveX = 0
        self.moveY = 0

    def control(self, x, y):
        self.moveX += x
        self.moveY += y

    def update(self):
        self.rect.x = self.x + self.moveX
        self.rect.y = self.y + self.moveY


