import pygame as g


class Button:
    def __init__(self, text, pos, size, color, hover_color):
        self.text = text
        self.pos = pos
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.font = g.font.Font(None, size)
        self.rect = self.font.render(text, True, color).get_rect(center=pos)

    def draw(self, screen):
        mouse_pos = g.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            text = self.font.render(self.text, True, self.hover_color)
        else:
            text = self.font.render(self.text, True, self.color)
        screen.blit(text, self.rect)

    def is_clicked(self, event):
        if event.type == g.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(g.mouse.get_pos()):
                return True
        return False
