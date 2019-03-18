from levels.Level import Level
from levels.objects.player import Player
import pygbutton


class MainMenu(Level):
    def __init__(self, surface, lm, im):
        self.name = 'mainmenu'
        self.surface = surface
        self.lm = lm
        self.im = im
        self.p = Player()
        super().__init__(self.name, surface, lm)

        # Required so elements can scale according to size rather than have absolute size
        self.width, self.height = surface.get_size()
        self.buttons = []  # To store buttons for easy access in event_update

        # Crude way to create buttons but works, notice that the dimensions are a portion of height/width
        self.buttons.append(pygbutton.PygButton((self.width/3, self.height/8, self.width/3, 70), 'Play'))
        self.buttons.append(pygbutton.PygButton((self.width / 3, 2 * self.height / 8, self.width / 3, 70), 'Options'))
        self.buttons.append(pygbutton.PygButton((self.width / 3, 3 * self.height / 8, self.width / 3, 70), 'Credits'))

        # Stupid way to make my life easier to switch levels, not necessary
        self.button_functions = {'Options': 'options', 'Play': 'lobby', 'Credits': 'credits'}

    def draw(self):
        super().draw() # Standard super call in case we add anything to all levels
        self.surface.fill((255, 255, 255))
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
                self.lm.set_level(self.button_functions[b.caption])




class Credits(Level):
    def __init__(self, surface, lm):
        self.name = 'credits'
        super().__init__(self.name, surface, lm)

    def draw(self):
        self.surface.fill((255, 255, 255))
        print('Declan, Tommy, John')
