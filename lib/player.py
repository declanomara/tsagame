import pygame


class Player:
    def __init__(self, texture='lib/player.png', x=0, y=0):
        self.x = x
        self.y = y
        self.texture = pygame.image.load(texture)
        self.rect = self.texture.get_rect()
        self.base_movement_speed = 1

    def move(self, direction, timedelta):
        pass

    def draw(self, surface):
        surface.blit(self.texture, self.rect)




