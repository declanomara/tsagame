class LevelManager:
    def __init__(self, levels: dict):
        self.levels = levels
        self.current_level = None

    def set_level(self, level_name):
        self.current_level = self.levels[level_name]


class InputManager:
    def __init__(self, pygame):
        self.keys_down = []
        self.pygame = pygame

    def update_pressed(self):
        keys = self.pygame.key.get_pressed()
        buttons = []
        for i, k in enumerate(keys):
            if k == 1:
                buttons.append(self.pygame.key.name(i))
        self.keys_down = buttons

    def is_pressed(self, key):
        return key in self.keys_down
