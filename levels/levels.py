import lib.pygbutton as pygbutton
import sys
import pygame
import os

from run import resource_path
from levels.Level import Level
from levels.objects.player import Player


class MainMenu(Level):
    def __init__(self, surface, lm, im):
        self.name = 'mainmenu'
        self.surface = surface
        self.lm = lm
        self.im = im
        super().__init__(self.name, surface, lm)

        # Required so elements can scale according to size rather than have absolute size
        self.width, self.height = surface.get_size()
        self.buttons = []  # To store buttons for easy access in event_update

        self.p = Player(x=self.width/4, y=7*self.height/15)
        self.p.scale = self.height/15 * 3
        self.background = pygame.transform.scale(pygame.image.load(resource_path(os.path.join('resources', 'mainmenubackground.png'))),
                                                 (self.width, self.height))

        # Crude way to create buttons but works, notice that the dimensions are a portion of height/width
        self.buttons.append(
            pygbutton.PygButton((self.width / 3, 7 * self.height / 15, self.width / 3, self.height / 16), 'Play'))

        self.buttons.append(
            pygbutton.PygButton((self.width / 3, 8 * self.height / 15, self.width / 3, self.height / 16), 'Options'))

        self.buttons.append(
            pygbutton.PygButton((self.width / 3, 9 * self.height / 15, self.width / 6, self.height / 16), 'Credits'))

        self.buttons.append(
            pygbutton.PygButton((self.width / 2, 9 * self.height / 15, self.width / 6, self.height / 16), 'Quit'))

    def draw(self):
        super().draw() # Standard super call in case we add anything to all levels
        self.surface.fill((255, 255, 255))
        self.surface.blit(self.background, self.background.get_rect())

        self.p.draw(self.surface)
        for obj in self.buttons:
            obj.draw(self.surface)



    def update(self, timedelta):
        super().update(timedelta) # See draw method

        direction = {'x': 0, 'y': 0}
        val = {'a': -1, 'd': 1, 's': 1, 'w': -1}
        # We have nothing to update each frame so doesn't need any fancy code here

        for key in self.im.keys_down:
            if key in 'ad':
                direction['x'] += val[key]

            if key in 'ws':
                direction['y'] += val[key]

        self.p.move(direction, timedelta)

    def event_update(self, event):
        super().event_update(event) # See draw methods

        for b in self.buttons: # Just handling click events on buttons
            if 'click' in b.handleEvent(event):

                if b.caption == 'Play':
                    self.lm.set_level('lobby', data={'player': {'x': self.width/8 + 1, 'y': 1}})

                elif b.caption == 'Options':
                    self.lm.set_level('options')

                if b.caption == 'Credits':
                    self.lm.set_level('credits')

                if b.caption == 'Quit':
                    sys.exit(1)


class Credits(Level):
    def __init__(self, surface, lm):
        self.name = 'credits'
        super().__init__(self.name, surface, lm)

    def draw(self):
        self.surface.fill((255, 255, 255))
        # print('Declan, Tommy, John')
        print(self.data)


class Lobby(Level):
    def __init__(self, surface, lm, im):
        self.name = 'lobby'
        self.surface = surface
        self.lm = lm
        self.im = im
        self.data = None
        super().__init__(self.name, self.surface, self.lm)

        self.width, self.height = self.surface.get_size()
        self.player_x = self.width/4
        self.player_y = 7*self.height/15

        self.checked_data = False

        self.background = pygame.transform.scale(pygame.image.load(resource_path(os.path.join('resources', 'mainmenubackground.png'))), (self.surface.get_width() * 2, self.surface.get_height()) )
        self.p = Player(x=self.player_x, y=self.player_y)
        self.p.scale = self.height / 15 * 3

        self.floor_height = 7 * self.height / 15 + self.p.get_height()

        self.background_x = 0

    def draw(self):
        self.surface.blit(self.background, pygame.Rect(self.background_x, 0, self.width, self.height))
        self.p.draw(self.surface)

    def update(self, timedelta):
        if not self.checked_data:
            print('Checking for data')
            try:
                self.player_x = self.data['player']['x']
                self.player_y = self.data['player']['y']
                self.p.place(self.player_x, self.player_y)
                # print(f'Player at {self.player_x, self.player_y}')
                # print(self.data)

            except TypeError:
                # print(self.data)
                # print('TypeError')
                pass

            except KeyError:
                # print(self.data)
                # print('KeyError')
                pass

            self.checked_data = True

        direction = {'x': 0, 'y': 0}
        val = {'a': -1, 'd': 1, 's': 1, 'w': -1}
        # We have nothing to update each frame so doesn't need any fancy code here

        for key in self.im.keys_down:
            if key == 'a':
                if self.width/8 < self.p.x:
                    direction['x'] += -1

                elif self.background_x < 0:
                    self.background_x += self.p.base_movement_speed['x'] * timedelta * 1000


            if key == 'd':
                if self.p.x < self.width - self.width/8:
                    direction['x'] += 1

                elif self.background_x > -self.width:
                    self.background_x -= self.p.base_movement_speed['x'] * timedelta * 1000

        if self.p.y < self.floor_height - self.p.get_height():
            direction['y'] = 1

        self.p.move(direction, timedelta)

        super().update(timedelta)


class Trivia(Level):
    def __init__(self, surface, lm):
        self.name = 'trivia'
        self.surface = surface
        self.lm = lm
        super().__init__(self.name, self.surface, self.lm)

        self.doorwayTexture = pygame.image.load('levels/objects/doorway.png')
        self.doorways = ['A', 'B', 'C']

        self.options = ['Animation', 'Coding', 'Music', 'Video Games']

        self.buttons = []

    def draw(self):
        # self.surface.blit(self.background, self.background.get_rect())
        # self.p.draw(self.surface)
        pass

    def update(self, timedelta):
        if pygame.sprite.collide_rect(Player, self.doorways[1]):
            print('Player has entered door and will do X trivia')



