from ui.label import Label
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.color import WHITE
from game_state import GameState

import pygame


class MainMenu:
    def __init__(self, screen: pygame.Surface, fps: int):
        self.screen = screen
        self.fps = fps

    def run(self):
        clock = pygame.time.Clock()

        lbl_play = Label(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2, "PLAY :)", font_size=80)
        lbl_quit = Label(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 + 50, "QUIT :c", font_size=80)
        
        while(True):
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return GameState.QUIT
                
                left_mouse, mouse_wheel, right_mouse = pygame.mouse.get_pressed()

                if left_mouse:
                    if lbl_play.has_been_clicked(mouse_pos):
                        return GameState.TEST_LEVEL
                    if lbl_quit.has_been_clicked(mouse_pos):
                        return GameState.QUIT
        
            lbl_play.update(mouse_pos)
            lbl_quit.update(mouse_pos)

            self.screen.fill(WHITE)

            lbl_play.draw(self.screen)
            lbl_quit.draw(self.screen)
        
            # utility
            pygame.display.flip()
            clock.tick(self.fps)