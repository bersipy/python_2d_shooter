from ui.label import Label
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game_state import GameState

import pygame
from OpenGL.GL import GL_COLOR_BUFFER_BIT, glClear, glLoadIdentity

class MainMenu:
    def __init__(self, fps: int):
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

            glClear(GL_COLOR_BUFFER_BIT)
            glLoadIdentity()

            lbl_play.draw()
            lbl_quit.draw()
        
            # utility
            pygame.display.flip()
            clock.tick(self.fps)
