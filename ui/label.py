from utils.color import BLACK, PINK, rgb_to_gl_color
from typing import Tuple

import pygame
from OpenGL.GL import *


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
        self.texture = None  # Store OpenGL texture
        self.width = 0  # Text width for alignment
        self.height = 0  # Text height for alignment
        self.update_texture()

    def update_texture(self):
        """
        Converts the text to an OpenGL texture.
        """
        # Render text to Pygame surface
        surface = self.font.render(self.text, True, self.color)
        self.width, self.height = surface.get_size()
        
        # Convert surface to string buffer
        texture_data = pygame.image.tostring(surface, "RGBA", True)
        
        # Generate and bind the texture
        if self.texture is None:
            self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        
        # Upload texture data
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.width, self.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
        
        # Set texture parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    def draw(self):
        self.color = PINK if self.is_highlighted else self.default_color
        
        # Create new texture with current color
        surface = self.font.render(self.text, True, self.color)
        texture_data = pygame.image.tostring(surface, "RGBA", True)
        
        # Bind and update texture
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.width, self.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
        
        # Enable texturing and blending
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        # Draw textured quad
        glBegin(GL_QUADS)
        glTexCoord2f(0, 1); glVertex2f(self.x, self.y)
        glTexCoord2f(1, 1); glVertex2f(self.x + self.width, self.y)
        glTexCoord2f(1, 0); glVertex2f(self.x + self.width, self.y + self.height)
        glTexCoord2f(0, 0); glVertex2f(self.x, self.y + self.height)
        glEnd()
        
        # Disable texturing
        glDisable(GL_TEXTURE_2D)

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
