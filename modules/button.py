import pygame as g
from .values import *


class Button:
    def __init__(self, text, pos, size, color, hover_color, border_color, border_thickness):
        self.text = text
        self.pos = pos
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.font = g.font.Font(None, size)
        self.rect = g.Rect((pos[0] - 100), (pos[1] - 20), 200, 40)

    def draw(self, screen):
        mouse_pos = g.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            current_color = self.hover_color
        else:
            current_color = self.color

        text_surf = self.font.render(self.text, True, current_color)
        text_rect = text_surf.get_rect(center=self.pos)

        # Draw border with rounded corners
        g.draw.rect(screen, self.border_color, self.rect, border_radius=15)
        # Draw button with rounded corners inside the border
        inner_rect = self.rect.inflate(-self.border_thickness, -self.border_thickness)
        g.draw.rect(screen, BUTTON_COLOR, inner_rect, border_radius=15)

        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == g.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(g.mouse.get_pos()):
                return True
        return False
