import pygame
from run import resource_path

class Player:
    def __init__(self, texture='resources\\player.png', x=0, y=0):
        self.x = x
        self.y = y
        self.texture = pygame.image.load(resource_path(texture))
        self.rect = self.texture.get_rect()
        self.base_movement_speed = {'x': 1, 'y': 1}
        self.scale = 64

    def move(self, direction, timedelta):
        self.x += self.base_movement_speed['x'] * direction['x'] * timedelta * 1000
        self.y += self.base_movement_speed['y'] * direction['y'] * timedelta * 1000

    def draw(self, surface):
        width = int(self.scale/2)
        height = int(self.scale)
        rect = pygame.Rect(self.x, self.y, width, height)
        t = pygame.transform.scale(self.texture, (width, height))
        surface.blit(t, rect)




