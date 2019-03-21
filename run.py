import datetime
import sys
import os
from lib.managers import *
from levels.levels import *
from pygame.locals import *

if __name__ == '__main__':
    if getattr(sys, 'frozen', False):
        print('Running from .exe, not source')
    else:
        print('Running from source, using resources/')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    try:
        # TODO: replace FPS and RES with some sort of options manager
        FPS = 60  # FPS to run the game at
        RES = (1920//1, 1080//1)  # Resolution of the window, 1080p

        # Window setup
        pygame.init()
        windowSurface = pygame.display.set_mode(RES, 0, 32)
        pygame.display.set_caption('TSA GAME')
        clock = pygame.time.Clock()

        i = InputManager(pygame)  # Input manager, keystrokes and mouse

        previous_time = datetime.datetime.now()  # Used to get time delta, crucial for keeping movement speed consistent

        # Initially load all levels

        lm = LevelManager()

        MainMenu = MainMenu(windowSurface, lm, i)
        Credits = Credits(windowSurface, lm)
        Lobby = Lobby(windowSurface, lm, i)
        Trivia = Trivia(windowSurface, lm)
        DragRacing = DragRacing(windowSurface, lm, i)
        Options = Options(windowSurface, lm)

        lm.add_level('mainmenu', MainMenu)
        lm.add_level('credits', Credits)
        lm.add_level('options', Options)
        lm.add_level('lobby', Lobby)
        lm.add_level('level_0', DragRacing)
        lm.add_level('level_1', Trivia)

        lm.set_level('mainmenu')

        p = Player()
        p.draw(windowSurface)

        while True:

            # Time delta and FPS
            clock.tick(FPS)
            current_time = datetime.datetime.now()
            time_delta = current_time - previous_time
            previous_time = current_time

            # Updating managers
            i.update_pressed()

            # Load current level
            lm.current_level.update(time_delta.total_seconds())
            for event in pygame.event.get():
                lm.current_level.event_update(event)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()


            pygame.display.update()

    except ConnectionAbortedError:
        sys.exit(1)
