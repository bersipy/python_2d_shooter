from ui.label import Label
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.color import WHITE

import pygame


class MainMenu:
    def __init__(self, screen: pygame.Surface, fps: int):
        self.screen = screen
        self.fps = fps

    def run(self):
        clock = pygame.time.Clock()

        play = Label(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, "Play", font_size=80)
        while(True):
            self.screen.fill(WHITE)

            play.draw(self.screen)
        
            # utility
            pygame.display.flip()
            clock.tick(self.fps)