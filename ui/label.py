from utils.color import BLACK

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
        self.color = color

    def draw(self, screen):
        surface = self.font.render(self.text, True, self.color)
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