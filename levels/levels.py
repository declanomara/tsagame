import lib.pygbutton as pygbutton
import sys
import pygame
import os
import datetime

from run import resource_path
from levels.Level import Level
from levels.objects.player import Player
from levels.objects.car import Car
from lib.render_text import Text


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
        self.background = pygame.transform.scale(pygame.image.load(resource_path(os.path.join('resources', 'mainmenubackground_0.png'))),
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
        self.surface = surface
        self.lm = lm
        super().__init__(self.name, surface, lm)

        self.width, self.height = surface.get_size()

        self.text_rect = pygame.Rect(self.width/4, self.height/4, self.width/2, self.height/2)

    def draw(self):

    def

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

        self.background = pygame.transform.scale(pygame.image.load(resource_path(os.path.join('resources', 'lobbybackground.png'))), (self.surface.get_width() * 2, self.surface.get_height()))
        self.nature = pygame.transform.scale(pygame.image.load(resource_path(os.path.join('resources', 'nature.jpg'))), (self.surface.get_width() * 3, self.surface.get_height()))
        self.p = Player(x=self.player_x, y=self.player_y)
        self.p.scale = self.height / 15 * 3

        self.floor_height = 7 * self.height / 15 + self.p.get_height()

        self.background_x = 0

        self.doors = [pygame.image.load(resource_path(os.path.join('resources', 'door.png'))) for x in range(3)]

        self.text_rect = pygame.Rect(self.width/8 + self.p.get_width(), self.floor_height + self.p.get_height(), self.width - self.width/4 - self.p.get_width() * 2, self.height - self.floor_height + self.p.get_height())
        self.sign_text = Text('Enter levels by pressing "w" in front of the door. To win the TSA competition, you must beat all levels! Good luck! \n Press ENTER to continue.', self.text_rect)
        self.tutorial_text = Text('Move through the main hallway using "A" and "D" keys \nPress ENTER to continue.', self.text_rect)

        self.tutorial = True
        self.sign_prompt = False
        self.has_prompted = False

        self.alert_rect = pygame.Rect(self.width/4, self.height/4, self.width/2, self.height/2)
        self.alerts = []

        self.alert_up = False
        self.current_alert = None

        self.incoming_data = False

    def draw(self):
        self.surface.blit(self.nature, pygame.Rect(self.background_x * 1.1 - self.p.get_width() * 3, -self.p.get_height()/3*2, self.width, self.height))
        self.surface.blit(self.background, pygame.Rect(self.background_x, 0, self.width, self.height))

        for i, door in enumerate(self.doors):
            d = pygame.transform.scale(door, (int(self.p.get_width()*3/2), int(self.p.get_height() * 4/3)))
            rect = pygame.Rect(self.width/3 * i + self.background_x + self.width + self.p.get_width() * 1.5, self.floor_height - self.p.get_height() * 17/12, self.width/6, self.p.get_height()*4/3)
            self.surface.blit(d, rect)

            if rect.colliderect(pygame.Rect(self.p.x, self.p.y, self.p.get_width(), self.p.get_height())):
                if self.im.is_pressed('w'):
                    if not self.lm.get_level(f'level_{i}').completed:
                        self.lm.set_level(f'level_{i}')

        self.p.draw(self.surface)

        if self.tutorial:
            self.tutorial_text.render(self.surface)

        if self.sign_prompt:
            self.sign_text.render(self.surface)


        # pygame.draw.rect(self.surface, (255,0,0), self.text_rect)


    def update(self, timedelta):
        self.floor_height = 7 * self.height / 15 + self.p.get_height()
        if self.incoming_data:
            print('Checking for data')
            try:
                if 'player' in self.data:
                    self.player_x = self.data['player']['x']
                    self.player_y = self.data['player']['y']
                    self.p.place(self.player_x, self.player_y)
                if 'alerts' in self.data:
                    print(self.alerts, self.data['alerts'])
                    if self.data['alerts']:
                        self.alerts.extend(self.data['alerts'])



                # print(f'Player at {self.player_x, self.player_y}')
                # print(self.data)

            except TypeError as e:
                # print(self.data)
                # print('TypeError')
                print(e)
                pass

            except KeyError as e:
                # print(self.data)
                print(e)
                pass

            self.incoming_data = False

            self.draw()

        if not self.alert_up and self.alerts:
            self.current_alert = self.alerts.pop()
            print('Current alert ' + self.current_alert)
            self.alert_up = True

            return

        if self.alert_up:
            t = Text(self.current_alert, self.alert_rect)
            t.render(self.surface)

            if self.im.is_pressed('return'):
                self.current_alert = None
                self.alert_up = False

            return



        direction = {'x': 0, 'y': 0}
        val = {'a': -1, 'd': 1, 's': 1, 'w': -1}

        # print(self.background_x)
        if not self.tutorial and not self.sign_prompt:
            for key in self.im.keys_down:
                if key == 'a':
                    if self.width/8 + self.p.get_width() < self.p.x + self.p.movement_speed['x'] * timedelta:
                        direction['x'] += -1

                    elif self.background_x < 0 - self.p.movement_speed['x'] * timedelta:
                        self.background_x += self.p.movement_speed['x'] * timedelta


                if key == 'd':
                    if self.p.x + self.p.movement_speed['x'] * timedelta < self.width - self.width/8 - self.p.get_width():
                        direction['x'] += 1

                    elif self.background_x > -self.background.get_width()/2:
                        self.background_x -= self.p.movement_speed['x'] * timedelta

                    if self.background_x < -self.background.get_width()/2:
                        self.background_x = -self.background.get_width()/2

        else:
            self.sign_text.render(self.surface)

            if self.im.is_pressed('return') and not self.alert_up:
                self.tutorial = False
                self.sign_prompt = False

        if self.p.y < self.floor_height - self.p.get_height():
            direction['y'] = 1

        self.p.move(direction, timedelta)

        if self.p.x < self.width/8:
            self.p.x = self.width/8

        if self.p.x > self.width - self.width/8 - self.p.get_width() * 1.1:
            self.p.x = self.width - self.width/8 - self.p.get_width() * 1.1

        if not self.has_prompted and self.player_pos() > self.background.get_width()/2:
            self.sign_prompt = True
            self.has_prompted = True

        super().update(timedelta)

    def player_pos(self):
        return int(self.p.x - self.background_x)


class DragRacing(Level):
    def __init__(self, surface, lm, im):
        self.name = 'level_0'
        self.surface = surface
        self.lm = lm
        self.im = im
        self.data = None
        super().__init__(self.name, self.surface, self.lm)

        self.width, self.height = self.surface.get_size()

        self.lights = [pygame.Rect(self.width * 1/9 + self.width/3 * i, self.height/12, self.width/20, self.width/20) for i in range(3)]
        self.colors = [(255,255,0),(255,255,0),(0,255,0)]

        self.p_car = Car(y=self.height * 4/16)
        self.o_car = Car(y =self.height * 6/16)

        self.p_car.rect = pygame.Rect(self.p_car.x, self.p_car.y, self.width/4, self.height/4)
        self.o_car.rect = pygame.Rect(self.o_car.x, self.o_car.y, self.width/4, self.height/4)

        self.info_rect = pygame.Rect(self.width/8, self.height * 3/4, self.width * 3/4, self.height/4)
        self.info = Text('Tap the space bar as each light changes color. On the green light, the race begins. Good luck! \nPress ENTER to continue.', self.info_rect)

        self.light = -1

        self.has_prompted = False
        self.is_prompting = False
        self.last_time = None

        self.was_down = False

        self.times = []
        self.light_times = []

        self.completed = False

        self.simulating = False
        self.simulated = False

    def draw(self):
        self.surface.fill(255)
        self.p_car.draw(self.surface)
        self.o_car.draw(self.surface)

        for i,l in enumerate(self.lights):
            pygame.draw.rect(self.surface, (255, 0, 0), l)

        for i,l in enumerate(self.lights):
            if self.light >= i:
                pygame.draw.rect(self.surface, self.colors[i], l)

        current_time = datetime.datetime.now()
        if self.last_time and (current_time - self.last_time).total_seconds() > 1 and self.light < 2:
            self.last_time = current_time
            self.light += 1
            self.light_times.append(current_time)



    def update(self, timedelta):
        super().update(timedelta)
        if self.simulating:
            self.p_car.update(timedelta)
            self.o_car.update(timedelta)

            self.draw()

            if self.o_car.x > self.width or self.p_car.x > self.width:
                print('DONE')

                data = {}
                if self.completed:
                    data = {'alerts': ['Congratulations, you won the first event: Drag Racing! \nPress ENTER to continue.']}
                else:
                    data = {'alerts': ['Unfortunately, you mistimed your taps. You may retry by entering the door again. \nPress ENTER to continue.']}

                self.lm.get_level('lobby').incoming_data = True
                self.lm.set_level('lobby', data=data)

            return

        if not self.has_prompted:
            self.info.render(self.surface)

            if not self.is_prompting:
                self.is_prompting = True


        if self.is_prompting:
            if self.im.is_pressed('return'):
                self.has_prompted = True
                self.is_prompting = False
                self.times.append(datetime.datetime.now())
                self.last_time = self.times[0]

            return

        if self.im.is_pressed('space'):
            self.was_down = True

        elif self.was_down:
            self.was_down = False
            self.times.append(datetime.datetime.now())

        if len(self.times) >= 4:
            if len(self.light_times) == 3:
                diff =[]
                for i, t in enumerate(self.times[1:4]):
                    diff.append(abs((self.light_times[i] - self.times[1:][i]).total_seconds()))
                print(f'1: {diff[0]}, 2: {diff[1]}, 3: {diff[2]}')

                if sum(diff) > 1.5:
                    self.simulating = True
                    self.p_car.acceleration = .8 * 100

                    self.lm.remove_level('level_0')
                    self.lm.add_level('level_0', DragRacing(self.surface, self.lm, self.im))

                else:
                    self.p_car.acceleration = 1.2 * 100
                    self.completed = True
                    self.simulating = True



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



