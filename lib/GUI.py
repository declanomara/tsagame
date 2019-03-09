import pygame

pygame.init()
pygame.font.init()


class Button:
    def __init__(self, x, y, w, h, label, font='Comic Sans MS', size=24):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.rect_outer = pygame.Rect(x, y, w, h)
        self.label = label
        self.font = pygame.font.SysFont(font, size)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.rect_outer)
        textsurface = self.font.render(self.label, False, (255, 255, 255))
        surface.blit(textsurface, (self.x + 3, self.y - 3))
