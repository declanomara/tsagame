'''
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
'''


class Player:
    def __init__(self, texture, x=0, y=0):
        self.x = x
        self.y = y
        self.base_movement_speed = 1

    def move(self, direction, timedelta):
        pass



