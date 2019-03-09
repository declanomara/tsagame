from levels.Level import Level
from lib.GUI import Button


class MainMenu(Level):
    def __init__(self):
        self.name = 'mainmenu'
        super().__init__(self.name)
        pass

    def draw(self, surface):
        surface.fill((255, 255, 255))
        b = Button(20,20,100,30,'example')
        b.draw(surface)



if __name__ == '__main__':
    m = MainMenu()