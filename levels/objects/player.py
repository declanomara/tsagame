import pygame


class Player:
    def __init__(self, texture='levels/objects/player.png', x=0, y=0):
        self.x = x
        self.y = y
        self.texture = pygame.image.load(texture)
        self.rect = self.texture.get_rect()
        self.base_movement_speed = {'x': 1, 'y': 1}
        self.scale = 20

    def move(self, direction, timedelta):
        self.x += self.base_movement_speed['x'] * direction['x'] * timedelta * 1000
        self.y += self.base_movement_speed['y'] * direction['y'] * timedelta * 1000
        print(self.base_movement_speed['y'] * direction['y'] * timedelta * 1000, direction['y'])

    def draw(self, surface):
        scale = self.scale
        x, y = surface.get_size()
        width = int(x/scale)
        height = width*2
        rect = pygame.Rect(self.x, self.y, width, height)
        t = pygame.transform.scale(self.texture, (width, height))
        surface.blit(t, rect)




