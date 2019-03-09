import pygame
import datetime
import sys
import inspect
from lib.managers import *
from levels.levels import *
from pygame.locals import *

if __name__ == '__main__':
    # TODO: replace FPS and RES with some sort of options manager
    FPS = 120  # FPS to run the game at
    RES = (1920, 1080)  # Resolution of the window, 1080p

    # Window setup
    pygame.init()
    windowSurface = pygame.display.set_mode(RES, 0, 32)
    pygame.display.set_caption('TSA GAME')
    clock = pygame.time.Clock()

    i = InputManager(pygame)  # Input manager, keystrokes and mouse

    previous_time = datetime.datetime.now()  # Used to get time delta, crucial for keeping movement speed consistent

    # Initially load all levels
    MainMenu = MainMenu()
    lm = LevelManager({'mainmenu': MainMenu})
    lm.set_level('mainmenu')

    while True:
        # Time delta and FPS
        clock.tick(FPS)
        current_time = datetime.datetime.now()
        time_delta = current_time - previous_time
        previous_time = current_time

        # Updating managers
        i.update_pressed()

        # Load current level
        lm.current_level.draw(windowSurface)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
