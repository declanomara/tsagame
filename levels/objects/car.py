import pygame
import os
from run import resource_path


class Car:
    def __init__(self, x=0, y=0, texture=resource_path(os.path.join('resources', 'car.png'))):
        self.acceleration = 100
        self.velocity = 0
        self.x = x
        self.y = y

        self.texture = pygame.image.load(texture)
        self.rect = self.texture.get_rect()


    def update(self, timedelta):
        self.velocity += self.acceleration * timedelta
        self.x += int(self.velocity)

        self.rect = pygame.Rect(self.x, self.rect.y, self.rect.width, self.rect.height)


    def draw(self, surface):
        surface.blit(self.texture, self.rect)


