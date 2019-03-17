from levels.Level import Level
import pygbutton


class MainMenu(Level):
    def __init__(self, surface, lm):
        self.name = 'mainmenu'
        self.surface = surface
        self.lm = lm
        self.width, self.height = surface.get_size()
        self.i = 0
        self.buttons = []
        self.buttons.append(pygbutton.PygButton((self.width/3, self.height/8, self.width/3, 70), 'Play'))
        self.buttons.append(pygbutton.PygButton((self.width / 3, 2 * self.height / 8, self.width / 3, 70), 'Options'))
        self.buttons.append(pygbutton.PygButton((self.width / 3, 3 * self.height / 8, self.width / 3, 70), 'Credits'))
        self.button_functions = {'Options': 'options', 'Play': 'lobby', 'Credits': 'credits'}
        super().__init__(self.name, surface, lm)

        pass

    def draw(self):
        self.surface.fill((255, 255, 255))
        for obj in self.buttons:
            obj.draw(self.surface)

    def update(self):
        # self.i += 2
        super().update()

    def event_update(self, event):
        super().event_update(event)

        for b in self.buttons:
            # print(event)
            if 'click' in b.handleEvent(event):
                self.lm.set_level(self.button_functions[b.caption])
                # print(f'This button works we just have to implement a level named {self.button_functions[b.caption]}')


class Credits(Level):
    def __init__(self, surface, lm):
        self.name = 'credits'
        super().__init__(self.name, surface, lm)

    def draw(self):
        self.surface.fill((255, 255, 255))
        print('Declan, Tommy, John')