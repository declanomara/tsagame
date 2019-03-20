import pygame
import os
from run import resource_path

class Player:
    def __init__(self, texture=os.path.join('resources', 'player.png'), x=0, y=0):
        self.x = x
        self.y = y
        self.texture = pygame.image.load(resource_path(texture))
        self.rect = self.texture.get_rect()
        self.scale = 64
        self.base_movement_speed = {'x': 1 / 64, 'y': 1 / 48}
        self.movement_speed = {'x': self.base_movement_speed['x'] * self.scale * 1000, 'y': self.base_movement_speed['y'] * self.scale * 1000}

    def move(self, direction, timedelta):
        self.x += self.movement_speed['x'] * direction['x'] * timedelta
        self.y += self.movement_speed['y'] * direction['y'] * timedelta

    def draw(self, surface):
        width = int(self.scale/2)
        height = int(self.scale)
        rect = pygame.Rect(self.x, self.y, width, height)
        self.texture = pygame.transform.scale(self.texture, (width, height))
        surface.blit(self.texture, rect)

    def place(self, x, y):
        self.x = x
        self.y = y

    def get_height(self):
        return self.texture.get_height()

    def get_width(self):
        return self.texture.get_width()



