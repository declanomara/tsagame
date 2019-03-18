class Level:
    def __init__(self, name, surface, lm):
        self.name = name  # Name of the level
        self.surface = surface  # Pygame surface to draw to
        self.lm = lm  # Level manager, allows for levels to switch to another level. Crude but works.

    # Called every frame in the main loop
    def update(self, timedelta):
        self.draw()
        pass

    # Called for each event (mouse movement, keyboard input, etc. )
    def event_update(self, event):
        pass

    # Used to draw to the screen, called by update
    def draw(self):
        pass
