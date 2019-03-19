import pygame
from run import resource_path

class Player:
    def __init__(self, texture='resources\\player.png', x=0, y=0):
        self.x = x
        self.y = y
        self.texture = pygame.image.load(resource_path(texture))
        self.rect = self.texture.get_rect()
        self.scale = 64
        self.base_movement_speed = {'x': 1 / 32, 'y': 1 / 16}
        self.movement_speed = {'x': self.base_movement_speed['x'] * self.scale, 'y': self.base_movement_speed['y'] * self.scale}

    def move(self, direction, timedelta):
        self.x += self.base_movement_speed['x'] * direction['x'] * timedelta * 1000
        self.y += self.base_movement_speed['y'] * direction['y'] * timedelta * 1000

    def draw(self, surface):
        width = int(self.scale/2)
        height = int(self.scale)
        rect = pygame.Rect(self.x, self.y, width, height)
        t = pygame.transform.scale(self.texture, (width, height))
        surface.blit(t, rect)

    def place(self, x, y):
        self.x = x
        self.y = y

    def get_height(self):
        return self.texture.get_height()



