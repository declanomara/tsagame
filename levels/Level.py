class Level:
    def __init__(self, name, surface, lm):
        self.name = name
        self.surface = surface
        self.lm = lm

    def update(self):
        self.draw()
        pass

    def event_update(self, event):
        pass

    def draw(self):
        pass
