from utils.color import BLACK, PINK
from typing import Tuple

import pygame


class LabelAlignment:
    LEFT = 0
    CENTER = 1
    RIGHT = 2
    VALID = [LEFT, CENTER, RIGHT]


class Label:
    """
    A simple label.
    """
    def __init__(self, 
                 x: int = 20, 
                 y: int = 20, 
                 text: str = '', 
                 color: tuple[int, int, int] = BLACK, 
                 font_size: int = 50,
                 ):
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, font_size) 
        self.text = text
        self.default_color = self.color = color
        self.is_highlighted = False

    def draw(self, screen):
        color = self.default_color
        if self.is_highlighted:
            color = PINK
            
        surface = self.font.render(self.text, True, color)
        rect = surface.get_rect()
        rect.topleft = (self.x, self.y)
        screen.blit(surface, rect)

    def update_text(self, text: str):
        self.text = text

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y

    def change_color(self, color: tuple[int, int, int]):
        self.color = color

    @property
    def text_width(self):
        return self.font.size(self.text)[0]
    
    @property
    def text_height(self):
        return self.font.size(self.text)[1]
    
    def update(self, mouse_pos):
        if self.__has_mouse_hover(mouse_pos):
            self.highlight()
        else:
            self.unhighlight()

    def highlight(self):
        self.is_highlighted = True

    def unhighlight(self):
        self.is_highlighted = False

    def has_been_clicked(self, mouse_pos: Tuple[int, int]):
        return self.__has_mouse_hover(mouse_pos)

    def __has_mouse_hover(self, mouse_pos: Tuple[int, int]):
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        return self.x < mouse_x and (self.x + self.text_width) > mouse_x and self.y < mouse_y and (self.y + self.text_height) > mouse_y 
