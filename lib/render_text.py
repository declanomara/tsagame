import pygame as pg

def render_textrect(string, font, rect, text_color, background_color, justification=0):
    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException("The word " + word + " is too long to fit in the rect passed.")
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

    # write the text out on the surface.

    surface = pg.Surface(rect.size)
    # surface.fill(255)
    # surface.set_alpha(0)
    surface.fill(0)
    buffer = surface.get_width()//400
    pg.draw.rect(surface, (255,255,255), pg.Rect(buffer, buffer, surface.get_width() - buffer * 2, surface.get_height() - buffer * 2))

    accumulated_height = 0
    for line in final_lines:
        if accumulated_height + font.size(line)[1] >= rect.height:
            raise TextRectException("Once word-wrapped, the text string was too tall to fit in the rect.")
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            else:
                raise TextRectException("Invalid justification argument: " + str(justification))
        accumulated_height += font.size(line)[1]

    return surface

class Text:
    def __init__(self, text, screen_rect):
        self.text = text
        font = pg.font.SysFont("arial", 30)
        self.screen_rect = screen_rect
        self.image = render_textrect(text, font, screen_rect, (0,0,0), (255,255,255))
        self.rect = self.image.get_rect()

    def render(self, surf):
        width, height = self.image.get_size()
        rect = pg.Rect(self.screen_rect.left, self.screen_rect.top, width, height)
        surf.blit(self.image, rect)


def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight < rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text
if __name__ == '__main__':
    text = '''
    "Doubt that the sun doth move, doubt truth to be a liar, but never doubt I love". - (Act II, Scene II).
    '''

    pg.init()
    screen = pg.display.set_mode((400,300))
    screen_rect = pg.Rect(75, 0, 250, 300)

    obj = Text(text, screen_rect)
    done = False
    while not done:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                done = True
        obj.render(screen)
        pg.display.update()