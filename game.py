from game_state import GameState
from scene.test_level import TestLevel
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

import pygame


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Minecraft")
        self.state = GameState.TEST_LEVEL

    def run(self):
        while True:
            if self.state == GameState.TEST_LEVEL:
                self.state = TestLevel(self.screen, FPS).run()
                
            elif self.state == GameState.QUIT:
                pygame.quit()
                exit(0)